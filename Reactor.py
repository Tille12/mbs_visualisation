# -*- coding: utf-8 -*-
import typing
from typing import Dict
from typing import List
from Compound import COMPOUND
from Model import MODEL
class REACTOR(object):
    def __init__(self, volume: float, flowrate: float,
                 biomass_init: Dict[MODEL, float], compounds_init: Dict[COMPOUND, float],
                 biomass_inflow: Dict[MODEL, float] = None, compounds_inflow: Dict[COMPOUND, float] = None):
        self.__volume = volume
        self.__flowrate = flowrate
        self.__biomass_init = biomass_init
        self.__compounds_init = compounds_init
        self.__biomass_inflow = biomass_inflow
        self.__compounds_inflow = compounds_inflow

        # {'biomassInflow': array([[0.],
        #        [0.]]), 'biomassInit': array([[28.57142857],
        #        [21.42857143]]), 'compounds': ['Propionate', 'Acetate', 'Fumarate', 'Succinate', 'CO2', 'H2', 'Formate', 'Methane'], 'compoundsInflow': array([[0.],
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