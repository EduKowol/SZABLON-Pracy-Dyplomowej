"""Aproksymacja danych i eksport wykresu użytego w pracy."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "aproksymacja.csv"
OUTPUT_FILE = ROOT / "figures" / "aproksymacja-python.pdf"

data = np.genfromtxt(DATA_FILE, delimiter=",", names=True)
x = data["x"]
y = data["measurement"]

coefficients = np.polyfit(x, y, deg=1)
model = np.polyval(coefficients, x)
residuals = y - model
rmse = np.sqrt(np.mean(residuals**2))
r_squared = 1 - np.sum(residuals**2) / np.sum((y - np.mean(y)) ** 2)

fig, ax = plt.subplots(figsize=(6.4, 4.0), constrained_layout=True)
ax.scatter(x, y, color="black", marker="o", label="Pomiary")
ax.plot(x, model, color="#00467d", linewidth=2.0, label="Aproksymacja")
ax.set_xlabel("Wielkość wejściowa x")
ax.set_ylabel("Wielkość wyjściowa y")
ax.grid(True, alpha=0.3)
ax.legend()
fig.savefig(OUTPUT_FILE)

print(f"a={coefficients[0]:.6f}, b={coefficients[1]:.6f}")
print(f"RMSE={rmse:.6f}, R2={r_squared:.6f}")
