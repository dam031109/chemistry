
"""
Conductivity model for NaCl, KCl, MgCl2 (25 °C)
Reads params.csv and computes σ(c) using Kohlrausch law.
Outputs graphs and a summary table.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load parameters
df = pd.read_csv('params.csv')

# Concentration grid (mol L⁻¹)
c = np.linspace(0.001, 4.0, 4000)  # high resolution

results = []

for _, row in df.iterrows():
    name = row['Electrolyte']
    Lambda0 = row['Lambda0_cm2'] * 1e-4  # S m² mol⁻¹
    K = row['K_cm2'] * 1e-4             # S m² mol⁻¹ M⁻½

    Lambda_m = Lambda0 - K * np.sqrt(c)       # S m² mol⁻¹
    sigma = Lambda_m * c * 1000               # S m⁻¹

    idx_max = np.argmax(sigma)
    c_star = c[idx_max]
    sigma_max = sigma[idx_max]

    results.append({
        'Electrolyte': name,
        'c*_mol_L': round(c_star, 3),
        'sigma_max_S_m': round(sigma_max, 2)
    })

    plt.figure()
    plt.plot(c, sigma)
    plt.title(f'σ vs c for {name} at 25 °C')
    plt.xlabel('c (mol L⁻¹)')
    plt.ylabel('σ (S m⁻¹)')
    plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
    plt.tight_layout()
    plt.savefig(f'{name}_sigma_curve.png', dpi=150)
    plt.close()

summary = pd.DataFrame(results)
summary.to_csv('sigma_summary.csv', index=False)
print('--- Conductivity maxima summary ---')
print(summary.to_string(index=False))
print('\nGraphs saved as *_sigma_curve.png')
print('Summary table saved as sigma_summary.csv')
