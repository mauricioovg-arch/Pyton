import numpy as np
import matplotlib.pyplot as plt

# Generamos el dominio
x = np.linspace(0.1, 4, 400)
# Una función clásica con un hueco analítico: f(x) = (x^2 - 4) / (x - 2)
y = (x**2 - 4) / (x - 2) 

plt.figure(figsize=(8, 6))
plt.plot(x, y, label="Gráfica de f(x)", color="darkblue", linewidth=2)

# Marcamos el punto al que nos acercamos (que no necesariamente está en el dominio)
plt.scatter([2], [4], facecolors="none", edgecolors="red", s=120, label="Punto límite (Hueco en x=2)")

# Sombreado de vecindades (Ventanas de tolerancia)
plt.axvspan(1.5, 2.5, color="gray", alpha=0.2, label="Vecindad perforada en X (Control)")
plt.axhspan(3.5, 4.5, color="green", alpha=0.2, label="Vecindad en Y (Tolerancia epsilon)")

plt.title("Comportamiento Geométrico del Límite en el Plano R^2")
plt.xlabel("Eje X (Dominio)")
plt.ylabel("Eje Y (Codominio)")
plt.legend()
plt.grid(True)
plt.show()
