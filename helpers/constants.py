import numpy as np

TRACK_WIDTH = 12.0  # in meters
VEHICLE_WIDTH = 0.8  # in meters
SAFETY_BUFFER = 0.5  # in meters
BOUNDARY_WIDTH = (TRACK_WIDTH - VEHICLE_WIDTH) / 2 - SAFETY_BUFFER
TOTAL_TRACK_LENGTH =  3674.47906546904 #in meters1406.588630345694

DS_MAX = 20.0  # in meters
DS_MIN = 1.0  # in meters
V_MAX = 10  # in m/s
V_MIN = 0.0  # in m/s

N_D_MIN, N_D_MAX = 2, 4
N_V = 5
STD_DEV_V = 0.1  # in m/s

M = 100.0
L_WHEELBASE = 2.0
LAMBDA_INERTIA = 0.05
M_EFF = M * (1 + LAMBDA_INERTIA)
RHO = 1.225
CD_A = 0.08
C_R = 0.002
MU = 0.5
G = 9.81
ETA_FC = 0.55
LHV_H2 = 120e6

KAPPA_MAX = np.tan(np.deg2rad(30)) / L_WHEELBASE

TOTAL_TIME = 35 * 60  # in seconds
LAPS = 4
TIME_HORIZON = TOTAL_TIME / LAPS  # in seconds

ACC_MIN = -0.05
ACC_MAX = 0.5
MAX_JERK = 1.5
