# MOSFET cell: Iout vs Vin for the original and the shifted Vref
import os
import matplotlib.pyplot as plt
from pam8 import load_wrdata, iout_from_vout, corner_voltage, turn_on_voltage

runs = [("spice/mos_vref320.txt", "Vref = 0.320 V"),
        ("spice/mos_vref275.txt", "Vref = 0.275 V")]

for path, label in runs:
    vin, vout = load_wrdata(path)
    iout = iout_from_vout(vout)
    c = corner_voltage(vin, iout)
    t = turn_on_voltage(vin, iout)
    print(label, " corner (line):", round(c, 3), "V   turn-on (0.5 uA):", round(t, 3),
          "V   Iout(0):", round(iout[0] * 1e6, 2), "uA")
    plt.plot(vin, iout * 1e6, label=f"{label} (corner {c:.3f} V)")

plt.axvline(0.32, color="gray", ls="--", label="wanted corner 0.32 V")
plt.xlabel("Vin [V]")
plt.ylabel("Iout [uA]")
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
os.makedirs("results", exist_ok=True)
plt.savefig("results/cell_vref.png", dpi=200)
plt.show()