import os
import numpy as np
import matplotlib.pyplot as plt
from pam8 import D, X, LABELS, ALPHA, BETA, llr_exact, llr_maxlog

snr_db_list = [10, 0] 

r = np.linspace(-8 * D, 8 * D, 2001)
vin = ALPHA * r + BETA
vin_points = ALPHA * X + BETA
tick_labels = [f"{v:.2f}\n{''.join(map(str, lab))}" for v, lab in zip(vin_points, LABELS)]

fig, axes = plt.subplots(3, 2, figsize=(11, 9), sharex=True)

for col, snr_db in enumerate(snr_db_list):
    snr = 10 ** (snr_db / 10)
    exact = llr_exact(r, snr)
    maxlog = llr_maxlog(r, snr)

    for k in range(3):
        ax = axes[k, col]
        ax.plot(vin, exact[:, k], "k", label="exact")
        ax.plot(vin, maxlog[:, k], "g--", label="max-log")
        ax.plot(vin_points, np.zeros(8), "o", color="tab:blue")
        ax.axhline(0, color="gray", lw=0.5)
        ax.set_ylabel(f"LLR bit {k + 1}")
        ax.grid(alpha=0.3)

    axes[0, col].set_title(f"SNR = {snr_db} dB")
    axes[2, col].set_xticks(vin_points, tick_labels)
    axes[2, col].set_xlabel("Vin [V]")

axes[0, 0].legend()
plt.tight_layout()
os.makedirs("results", exist_ok=True)
plt.savefig("results/fig2_llrs.png", dpi=200)
plt.show()