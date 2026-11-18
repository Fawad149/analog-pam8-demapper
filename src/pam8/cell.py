import numpy as np


def load_wrdata(path):
    data = np.loadtxt(path)
    return data[:, 0], data[:, 1]


def iout_from_vout(vout, vdd=1.6, rout=3e3):
    return (vdd - vout) / rout


def corner_voltage(vin, iout, low=0.2, high=0.8):
    imax = np.max(iout)
    middle = (iout > low * imax) & (iout < high * imax)
    slope, offset = np.polyfit(vin[middle], iout[middle], 1)
    return -offset / slope

def turn_on_voltage(vin, iout, level=0.5e-6):
    """Largest Vin at which the cell still gives more than `level` amps."""
    return np.max(vin[iout > level])