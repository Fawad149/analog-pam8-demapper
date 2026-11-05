import numpy as np
from .constellation import X, LABELS


def simulate(snr_db, n, seed=1):
    """Send n random PAM-8 symbols through the noisy channel."""
    rng = np.random.default_rng(seed)
    sigma = np.sqrt(1 / (2 * 10 ** (snr_db / 10)))
    idx = rng.integers(0, 8, n)
    r = X[idx] + sigma * rng.standard_normal(n)
    return r, LABELS[idx]


def gmi(llrs, bits, s=1):
    """Bit-wise GMI (eq. 6 in Hemza). Gives one value per bit."""
    # penalty is log2(1 + e^-L) if the bit was 1 and log2(1 + e^L) if it was 0
    x = np.where(bits == 1, -s * llrs, s * llrs)
    penalty = np.logaddexp(0, x) / np.log(2)
    return 1 - penalty.mean(axis=0)


def gmi_best_s(llr, bits):
    """Try different scalings s and keep the best GMI (Ivanov eq. 7)."""
    best_gmi = -np.inf
    best_s = 1
    for s in np.arange(0.05, 5, 0.05):
        g = gmi(llr, bits, s)
        if g > best_gmi:
            best_gmi = g
            best_s = s
    return best_gmi, best_s