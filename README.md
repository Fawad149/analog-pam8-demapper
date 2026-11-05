# Analog PAM-8 demapper: software reproduction

Reproduction of results from Hemza et al., "A fully open-source implementation of an
analog PAM-8 demapper for high-speed communications" (ISCAS 2026), with background
from Ivanov et al., IEEE Trans. Inf. Theory, 2016.

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Run
```bash
pytest                                   # checks against hand calculations
python scripts/fig2_llrs.py              # Fig. 2 at 10 dB and 0 dB -> results/
python scripts/fig2_llrs.py --snr-db 10 3 --show
```

## Status
- [x] Fig. 2: exact vs max-log LLRs
- [ ] Fig. 4: GMI / rate penalty vs SNR (digital curves)
- [ ] Scaling experiments (optimal s per bit)
- [ ] Behavioural cell model
- [ ] ngspice simulations (IHP SG13G2)