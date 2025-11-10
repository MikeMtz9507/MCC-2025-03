import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Función objetivo (Sphere)
# -----------------------------
def sphere(x):
    return np.sum(x**2)

# -----------------------------
# Algoritmo de Búsqueda Local (Hill Climbing)
# -----------------------------
def hill_climbing(func, dim=2, bounds=(-5, 5), max_iter=200):
    # Solución inicial aleatoria
    current = np.random.uniform(bounds[0], bounds[1], dim)
    current_val = func(current)

    history = [current_val]

    for _ in range(max_iter):
        # Generar vecino aleatorio (pequeña perturbación)
        neighbor = current + np.random.normal(0, 0.1, size=dim)
        neighbor = np.clip(neighbor, bounds[0], bounds[1])
        neighbor_val = func(neighbor)

        # Si el vecino mejora, actualizar
        if neighbor_val < current_val:
            current, current_val = neighbor, neighbor_val

        history.append(current_val)

    return current, current_val, history

# -----------------------------
# Ejecutar Hill Climbing
# -----------------------------
if __name__ == "__main__":
    np.random.seed(42)
    best_sol, best_val, history = hill_climbing(sphere, dim=2)

    print("Mejor solución encontrada:", best_sol)
    print("Valor en esa solución:", best_val)

    # Gráfica de convergencia
    plt.plot(history)
    plt.xlabel("Iteración")
    plt.ylabel("Mejor valor encontrado")
    plt.title("Convergencia de Búsqueda Local (Hill Climbing)")
    plt.grid(True)
    plt.show()