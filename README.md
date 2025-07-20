
# Conductivity Model (NaCl · KCl · MgCl₂)

Simple Python script to estimate the conductivity (σ) of three common electrolytes at 25 °C 
using the Kohlrausch law.

## Files
| File | Purpose |
|------|---------|
| `params.csv` | Λ₀ and K parameters for each electrolyte (units: S cm² mol⁻¹) |
| `conductivity_model.py` | Reads `params.csv`, computes σ(c), saves curves & summary |
| `sigma_summary.csv` | Auto‑generated table of σ_max and c* for each electrolyte |
| `*_sigma_curve.png` | Auto‑generated σ–c plots for each electrolyte |

## Quick Start
```bash
# Clone repo (after you push)
git clone https://github.com/<YOUR_USERNAME>/conductivity-model.git
cd conductivity-model

# Run
python conductivity_model.py
```

The script prints a summary table and saves PNG graphs + CSV results in the same directory.

## Reference
Parameters from CRC Handbook (2024 ed.) and Harned & Owen (1950).
