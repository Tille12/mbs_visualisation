import scipy.io as sio
import os
import mat73
print(os.path.dirname(sio.__file__))
print(os.path.basename(sio.__file__))
print(sio.__file__)
dirname = os.path.join('Y:', 'Home', 'rauj', 'Documents', 'microbialsim')
mat_filename = 'simulatedTrajectory_21-Jan-2020 14_52_45.mat'
mat_filepath = os.path.join(dirname, mat_filename)
print(mat_filepath)
#mat_file = sio.loadmat(mat_filepath)
mat73_file = mat73.loadmat(mat_filepath)
print(len(mat73_file))
print(mat73_file.keys())
print(len(mat73_file["trajectory"]))
runtime = mat73_file["elapsedHours"].copy()
reactor = mat73_file["reactor"].copy()
trajectory = mat73_file["trajectory"].copy()
traj_keys = trajectory.keys()
print(traj_keys)
traj_FBA = trajectory["FBA"].copy()
print(type(traj_FBA))
traj_FBA_keys = traj_FBA.keys()
print(traj_FBA_keys)
print(type(traj_FBA["biomassReac"]))
print(trajectory["time"])
print(type(trajectory["time"]))