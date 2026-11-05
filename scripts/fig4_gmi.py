# Cost of the max-log approximation, measured with the GMI (like Fig. 4 in Hemza et al.)
import os
import numpy as np
import matplotlib.pyplot as plt
from pam8 import llr_exact, llr_maxlog, simulate, gmi, gmi_best_s

snr_db_list = np.arange(-10, 21)
n = 200_000

gmi_exact = []
gmi_maxlog = []
gmi_scaled = []

for snr_db in snr_db_list:
    snr = 10 ** (snr_db / 10)
    r, bits = simulate(snr_db, n)
    exact = llr_exact(r, snr)
    maxlog = llr_maxlog(r, snr)

    g_ex = gmi(exact, bits)
    g_ml = gmi(maxlog, bits)

    # max-log again, but with the best scaling for each bit
    g_sc = []
    s_best = []
    for k in range(3):
        g, s = gmi_best_s(maxlog[:, k], bits[:, k])
        g_sc.append(g)
        s_best.append(s)

    gmi_exact.append(g_ex)
    gmi_maxlog.append(g_ml)
    gmi_scaled.append(g_sc)
    print(snr_db, "dB  exact:", np.round(g_ex, 3), " max-log:", np.round(g_ml, 3),
          " best s:", np.round(s_best, 2))

# one row per SNR, one column per bit; average over the bits as in eq. (7)
gmi_exact = np.array(gmi_exact).mean(axis=1)
gmi_maxlog = np.array(gmi_maxlog).mean(axis=1)
gmi_scaled = np.array(gmi_scaled).mean(axis=1)

fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))

axes[0].plot(snr_db_list, gmi_exact, "k", label="exact")
axes[0].plot(snr_db_list, gmi_maxlog, "g--", label="max-log")
axes[0].plot(snr_db_list, gmi_scaled, "g:", label="max-log, best s")
axes[0].set_ylabel("GMI")

axes[1].plot(snr_db_list, 100 * (gmi_exact - gmi_maxlog) / gmi_exact, "g--", label="max-log")
axes[1].plot(snr_db_list, 100 * (gmi_exact - gmi_scaled) / gmi_exact, "g:", label="max-log, best s")
axes[1].set_ylabel("Rate penalty [%]")

for ax in axes:
    ax.set_xlabel("SNR [dB]")
    ax.grid(alpha=0.3)
    ax.legend()

plt.tight_layout()
os.makedirs("results", exist_ok=True)
plt.savefig("results/fig4_gmi.png", dpi=200)
plt.show()