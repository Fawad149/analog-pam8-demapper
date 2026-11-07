import numpy as np


def load_wrdata(path):
    """Read an ngspice wrdata file. Returns Vin and the first saved vector."""
    data = np.loadtxt(path)
    return data[:, 0], data[:, 1]


def iout_from_vout(vout, vdd=1.6, rout=3e3):
    """Cell output current from the output voltage: Iout = (VDD - Vout) / Rout."""
    return (vdd - vout) / rout


def corner_voltage(vin, iout, low=0.2, high=0.8):
    """Fit a straight line to the middle of the ramp (between 20% and 80% of
    the largest current) and return the Vin where that line reaches zero."""
    imax = np.max(iout)
    middle = (iout > low * imax) & (iout < high * imax)
    slope, offset = np.polyfit(vin[middle], iout[middle], 1)
    return -offset / slope

def turn_on_voltage(vin, iout, level=0.5e-6):
    """Largest Vin at which the cell still gives more than `level` amps."""
    return np.max(vin[iout > level])