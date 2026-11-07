from pam8 import iout_from_vout, corner_voltage, turn_on_voltage
import numpy as np

def test_iout_from_vout():
    # 30 mV across 3k is 10 uA
    assert np.isclose(iout_from_vout(1.57), 10e-6)


def test_corner_of_ideal_ramp():
    # ideal ramp: 0 above 0.32 V, rising 50 uA/V below, flat at 10 uA below 0.12 V
    vin = np.linspace(0, 0.64, 641)
    iout = 10e-6 * np.clip((0.32 - vin) / 0.2, 0, 1)
    assert np.isclose(corner_voltage(vin, iout), 0.32)

def test_turn_on_of_ideal_ramp():
    vin = np.linspace(0, 0.64, 641)
    iout = 10e-6 * np.clip((0.32 - vin) / 0.2, 0, 1)
    assert abs(turn_on_voltage(vin, iout) - 0.31) <= 0.0015