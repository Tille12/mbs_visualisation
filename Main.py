# -*- coding: utf-8 -*-
import os
import mat73
from typing import Dict
from State import STATE
from Reactor import REACTOR
from Compound import COMPOUND
from Model import MODEL
from Trajectory import TRAJECTORY
from CommandLineParser import parse_command_line

groups_h5 = ["elapsedHours", "reactor", "trajectory"]
# if __name__ == '__main__':
#     # Command line parsing
#     try:
#         args = parse_command_line()
#     except IOError:
#         args = {}
#         raise Exception("Error occured while passing the arguments from the command line!")
#     if args.syntax:
#         raise Exception("Please use proper syntax, use '-h' for more information!")
#
#     if not args.input:
#         raise Exception("Please provide input file(s) with preceding '-i' statement!")
#     else:
#         for i in range(len(args.input)):
#             if not os.path.isdir(os.path.dirname(args.input[i])) and not os.path.exists(args.input[i]):
#                 raise Exception("No such file with given path or filename!")
#             if not os.path.isdir(os.path.dirname(args.input[i])):
#                 file_path = os.path.abspath(args.input[i])
#             else:
#                 file_path = os.path.abspath(args.input[i])
#             # Log statement for the console about the input file
#             print("Input file path of file " + str(i) + ": " + file_path)

#################################################
# Ab hier wieder unter 'if __name__ ...' einrücken und bis ######## löschen
dirname = os.path.join('Y:', 'Home', 'rauj', 'Documents', 'microbialsim')
mat_filename = 'simulatedTrajectory_21-Jan-2020 14_52_45.mat'
file_path = os.path.join(dirname, mat_filename)
print("Input file path of file: " + file_path)
#################################################

file = mat73.loadmat(file_path)

# Read group "trajectory"
gr_trajectory = file["trajectory"].copy()  # FIXME: is $*.copy() even necessary?!
FBA = gr_trajectory["FBA"]     # FIXME: How to read these??!
# 'FBA': {'biomassReac': None, 'coupledReactions': None, 'exchangeReactions': None,
# 'flux_dev_sum': None, 'flux_sum': None, 'fluxes': None, 'modelName': None, 'ngamReac': None,
# 'reactorCompoundIDs': None}
biomass_traj = gr_trajectory["biomass"][0]          # 'biomass': array([[28.57142857, ..., 28.64924745]])
compound_names = gr_trajectory['compoundNames']     # 'compoundNames': ['Propionate', ... 'Fumarate']
compounds = [COMPOUND(compound_name, index) for index, compound_name in enumerate(compound_names)]
compounds_traj = gr_trajectory["compounds"][0]   # 'compounds': array([[1.46204e+00, ..., 1.4984e+00]])
model_names = gr_trajectory["modelNames"]   # 'modelNames': ['iSfu648', 'iMhu428']
models = [MODEL(model_name, index) for index, model_name in enumerate(model_names)]
mu_traj = gr_trajectory["mu"][0]                 # 'mu': array([[0.00509213, ..., 0.]])
timestamps = gr_trajectory["time"][0]             # 'time': array([[0., 0.002, ..., 0.0020137]])
time_pars = gr_trajectory["timePars"]
# 'timePars': {'FBAsolver': array(2.), 'SteadyStateAccuracy': array(1.e-05), 'absTol': array(1.e-09),
# 'doMassBalance': array(1.), 'doMin2PrevFlux': array(1.), 'dopFBA': array(1.), 'fluxTolerance': array(
# 1.e-06), 'maxDeviation': array(5.), 'maxRelaxValue': array(1.), 'minRelaxValue': array(1.e-11),
# 'minimalGrowth': array(1.e-06), 'myAccuracy': array(1.e-15), 'myBioAccuracy': array(1.e-15),
# 'nonNegative': array(0.), 'parallel': array(0.), 'readInitialStateFrom': '\x00\x00', 'recording':
# array(0.), 'relTol': array(1.e-09), 'saveLoadedModelsToFile': array(0.), 'solver': array(2.),
# 'solverType': array(0.), 'tend': array(1.), 'timeStepSize': array(0.002), 'trajectoryFile':
# 'simulatedTrajectory_21-Jan-2020 14_52_45.mat'}}
# NOTE: Nur so rum mit typing: $ *: ... = {}
# otherwise: $TypeError: '_GenericAlias' object d. not support item assignment
states: Dict[float, STATE] = {}
# Create Dict of STATEs
for t_index, timestamp in enumerate(timestamps):
    current_composition_biomass: Dict[MODEL, float] = {}
    current_composition_compounds: Dict[COMPOUND, float] = {}
    current_mu: Dict[MODEL, float] = {}
    for model in models:
        current_composition_biomass[model] = biomass_traj[t_index]
        if t_index == 0:
            current_mu[model] = None
        else:
            current_mu[model] = mu_traj[t_index-1]
    for cmp in compounds:
        current_composition_compounds[cmp] = compounds_traj
    states[timestamp] = STATE(timestamp, current_composition_biomass, current_mu,
                              current_composition_compounds)

# Read group "reactor"
gr_reactor = file["reactor"].copy()  # FIXME: is $*.copy() even necessary?!
# {'biomassInflow': array([[0.],
#        [0.]]), 'biomassInit': array([[28.57142857],
#        [21.42857143]]), 'compounds': ['Propionate', 'Acetate', 'Fumarate', 'Succinate', 'CO2', 'H2',
#        'Formate', 'Methane'], 'compoundsInflow': array([[0.],
#        [0.],
#        [0.],
#        [0.],
#        [0.],
#        [0.],
#        [0.],
#        [0.]]), 'compoundsInit': array([[2.000e+01],
#        [0.000e+00],
#        [0.000e+00],
#        [0.000e+00],
#        [8.215e-03],
#        [9.561e-04],
#        [0.000e+00],
#        [0.000e+00]]), 'flowRate': array(0.), 'volume': array(1.)}
# [0.         0.002      0.00201374 ... 0.99638493 0.99838493 1.00038493]
volume, flowrate = float(gr_reactor["volume"]), float(gr_reactor["flowRate"])
compounds_init: Dict[COMPOUND, float] = {}
compounds_inflow: Dict[COMPOUND, float] = {}
for index, cmp in enumerate(compounds):
    compounds_init[cmp] = gr_reactor["compoundsInit"][index]
    compounds_inflow[cmp] = gr_reactor["compoundsInflow"][index]
biomass_init: Dict[MODEL, float] = {}
biomass_inflow: Dict[MODEL, float] = {}
for index, model in enumerate(models):
    biomass_init[model] = gr_reactor["biomassInit"][index]
    biomass_inflow[model] = gr_reactor["biomassInflow"][index]

# Create REACTOR instance
reactor = REACTOR(volume, flowrate, biomass_init, compounds_init,
                  biomass_inflow=biomass_inflow, compounds_inflow=compounds_inflow)

# Create TRAJECTORY instance
trajectory = TRAJECTORY(os.path.basename(file_path), models, timestamps,
                        states, reactor, time_pars, compounds)
