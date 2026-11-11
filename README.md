# Analog PAM-8 demapper: software reproduction and analysis

Reproduction and analysis of Hemza et al., "A fully open-source implementation of an
analog PAM-8 demapper for high-speed communications" (ISCAS 2026), using Ivanov et al.,
"On the information loss of the max-log approximation in BICM systems"
(IEEE Trans. Inf. Theory, 2016) for the theory.

Author: <your name>

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest -v          # 10 tests, checked against hand calculations
```
Requires Python >= 3.10, numpy, matplotlib. Run the scripts from the project root;
figures are saved to `results/`.

## What reproduces what

| Script | Output | Slide |
|---|---|---|
| `scripts/fig2_llrs.py` | Exact vs max-log LLRs at 10 dB and 0 dB (Hemza Fig. 2) | 3 |
| `scripts/fig4_gmi.py` | GMI and rate penalty vs SNR, with and without best scaling s per bit (~30 s) | 4 |
| `scripts/cell_vref.py` | MOSFET cell: Vref = 0.320 vs 0.275 V, corner and turn-on voltage | 7, 9 |
| `scripts/cell_bjt.py` | BJT vs MOSFET ramp; BJT Q2 nodes (saturation) | 7 |

## Code
- `src/pam8/constellation.py`: PAM-8 points (E[X^2] = 0.5), Gray labels, r -> Vin mapping
- `src/pam8/llr.py`: exact (eq. 2) and max-log (eq. 3) LLRs
- `src/pam8/metrics.py`: channel simulation, bit-wise GMI (eq. 6), best-s search (Ivanov eq. 7)
- `src/pam8/cell.py`: read ngspice output, Iout from Vout, corner and turn-on voltage

## Circuit simulations (spice/)
xschem + ngspice-42 with the IHP SG13G2 open PDK; the schematics need the PDK to open.
- `decoderCell.sch` / `.sym`: MOSFET cell (Ibias = 10 uA, all devices W/L = 0.15/0.14 um)
- `decoderCellBJT.sch`: BJT cell (npn13G2 mirrors, Ibias = 100 uA, minimum-size PMOS)
- `decoderCellBJT1uW.sch`: BJT cell variant with wider PMOS (W = 1 um), exploratory
- `decoderCell_tb.sch`: testbench, DC sweep of Vin from 0 to 0.64 V
- `mos_vref320.txt`, `mos_vref275.txt`: ngspice `wrdata` output (Vin, vout), MOSFET cell
- `bjt_min.txt`: ngspice `wrdata` output (Vin, vout, Vin, A, Vin, B), BJT cell

The .txt files are included, so the Python scripts run without the PDK.