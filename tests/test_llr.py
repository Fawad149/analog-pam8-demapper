import numpy as np
from pam8 import D, X, LABELS, ALPHA, BETA, llr_exact, llr_maxlog


def test_energy():
    assert np.isclose(np.mean(X ** 2), 0.5)


def test_gray_code():
    for i in range(7):
        assert np.sum(LABELS[i] != LABELS[i + 1]) == 1


def test_vin_mapping():
    assert np.allclose(ALPHA * X[[0, -1]] + BETA, [0.04, 0.60])


def test_hand_calculation():
    # r = 2.5d at 10 dB
    r = 2.5 * D
    assert np.allclose(llr_exact(r, 10)[0], [3.47, 1.91, 0.59], atol=0.01)
    assert np.allclose(llr_maxlog(r, 10)[0], [2.86, 1.43, 0.48], atol=0.01)


def test_maxlog_scales_with_snr():
    r = np.linspace(-8 * D, 8 * D, 101)
    assert np.allclose(llr_maxlog(r, 10), 10 * llr_maxlog(r, 1))