# BJT vs MOSFET cell: ramp shape, and Q2 saturation in the BJT cell
import os
import numpy as np
import matplotlib.pyplot as plt
from pam8 import load_wrdata, iout_from_vout, corner_voltage, turn_on_voltage

# MOSFET cell, Vref = 0.32 V
vin_m, vout_m = load_wrdata("spice/mos_vref320.txt")
iout_m = iout_from_vout(vout_m)

# BJT cell, Vref = 0.32 V; columns: Vin, vout, Vin, A, Vin, B
data = np.loadtxt("spice/bjt_min.txt")
vin_b = data[:, 0]
iout_b = iout_from_vout(data[:, 1])
va = data[:, 3]
vb = data[:, 5]

for name, vin, iout in [("MOSFET", vin_m, iout_m), ("BJT", vin_b, iout_b)]:
    print(name, " corner (line):", round(corner_voltage(vin, iout), 3),
          "V   turn-on:", round(turn_on_voltage(vin, iout), 3),
          "V   Iout(0):", round(iout[0] * 1e6, 2), "uA")

fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))

# left: both ramps scaled to their own maximum, so the shapes can be compared
axes[0].plot(vin_m, iout_m / iout_m.max(), label="MOSFET (10 uA)")
axes[0].plot(vin_b, iout_b / iout_b.max(), label="BJT (100 uA)")
axes[0].axvline(0.32, color="gray", ls="--", label="Vref = 0.32 V")
axes[0].set_ylabel("Iout / max")

# right: node voltages in the BJT cell; when B drops below A, Q2's
# base-collector junction is forward biased (BJT saturation)
axes[1].plot(vin_b, va, label="node A (Q2 base)")
axes[1].plot(vin_b, vb, label="node B (Q2 collector)")
axes[1].plot(vin_b, va - vb, "k:", label="A - B (base-collector)")
axes[1].set_ylabel("Voltage [V]")

for ax in axes:
    ax.set_xlabel("Vin [V]")
    ax.grid(alpha=0.3)
    ax.legend()

plt.tight_layout()
os.makedirs("results", exist_ok=True)
plt.savefig("results/cell_bjt.png", dpi=200)
plt.show()