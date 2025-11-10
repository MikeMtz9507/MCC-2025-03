import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Función objetivo (Sphere)
# -----------------------------
def sphere(x):
    return np.sum(x**2)

# -----------------------------
# Búsqueda Local (Hill Climbing)
# -----------------------------
def local_search(x, func, bounds, max_iter=100):
    current = x.copy()
    current_val = func(current)

    for _ in range(max_iter):
        # Generar vecino
        neighbor = current + np.random.normal(0, 0.1, size=len(x))
        neighbor = np.clip(neighbor, bounds[0], bounds[1])
        neighbor_val = func(neighbor)

        # Mejorar si conviene
        if neighbor_val < current_val:
            current, current_val = neighbor, neighbor_val

    return current, current_val

# -----------------------------
# Búsqueda Local Iterada (ILS)
# -----------------------------
def iterated_local_search(func, dim=2, bounds=(-5, 5),
                          max_iter=50, local_iter=100):
    # Solución inicial aleatoria
    best = np.random.uniform(bounds[0], bounds[1], dim)
    best, best_val = local_search(best, func, bounds, local_iter)

    history = [best_val]

    for _ in range(max_iter):
        # Perturbación: mover fuerte la solución actual
        perturbed = best + np.random.normal(0, 1.0, size=dim)
        perturbed = np.clip(perturbed, bounds[0], bounds[1])

        # Búsqueda local desde la perturbación
        candidate, candidate_val = local_search(perturbed, func, bounds, local_iter)

        # Actualizar mejor solución si mejora
        if candidate_val < best_val:
            best, best_val = candidate, candidate_val

        history.append(best_val)

    return best, best_val, history

# -----------------------------
# Ejecutar ILS
# -----------------------------
if __name__ == "__main__":
    np.random.seed(42)
    best_sol, best_val, history = iterated_local_search(sphere, dim=2)

    print("Mejor solución encontrada:", best_sol)
    print("Valor en esa solución:", best_val)

    # Gráfica de convergencia
    plt.plot(history)
    plt.xlabel("Iteración")
    plt.ylabel("Mejor valor encontrado")
    plt.title("Convergencia de Búsqueda Local Iterada (ILS)")
    plt.grid(True)
    plt.show()
