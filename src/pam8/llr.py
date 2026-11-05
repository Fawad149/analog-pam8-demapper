import numpy as np
from .constellation import X, LABELS


def llr_exact(r, snr):
    r = np.atleast_1d(r)
    llrs = np.zeros((len(r), 3))
    for k in range(3):
        ones = X[LABELS[:, k] == 1]
        zeros = X[LABELS[:, k] == 0]
        num = np.logaddexp.reduce(-snr * (r[:, None] - ones) ** 2, axis=1)
        den = np.logaddexp.reduce(-snr * (r[:, None] - zeros) ** 2, axis=1)
        llrs[:, k] = num - den
    return llrs


def llr_maxlog(r, snr):
    """Max-log LLRs (eq. 3). Only the nearest '0' and nearest '1' point count."""
    r = np.atleast_1d(r)
    llrs = np.zeros((len(r), 3))
    for k in range(3):
        ones = X[LABELS[:, k] == 1]
        zeros = X[LABELS[:, k] == 0]
        dist0 = np.min((r[:, None] - zeros) ** 2, axis=1)
        dist1 = np.min((r[:, None] - ones) ** 2, axis=1)
        llrs[:, k] = snr * (dist0 - dist1)
    return llrs