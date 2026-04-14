"""
╔══════════════════════════════════════════════════════════════════════════════╗
║         SOLUCIONADOR UNIVERSAL DE EDOs — Euler Mejorado & RK4              ║
║                                                                              ║
║  Métodos disponibles:                                                        ║
║    • Euler Mejorado y Euler (Heun) — orden 2                                         ║
║    • Runge-Kutta de 4to orden (RK4) — orden 4                               ║
║                                                                              ║
║  INSTRUCCIONES DE USO:                                                       ║
║  1. Edita la sección ── CONFIGURACIÓN ── con tu ecuación y condiciones.     ║
║  2. Elige el método: "euler" o "rk4"                                         ║
║  3. Define los tamaños de paso en la lista H_LIST                            ║
║  4. Ejecuta:  python universal_ode_solver.py                                 ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import math

# ══════════════════════════════════════════════════════════════════════════════
#  ── CONFIGURACIÓN ────────────────────────────────────────────────────────────
# ══════════════════════════════════════════════════════════════════════════════

# Define tu ecuación diferencial y' = f(x, y)
# Ejemplos:
#   y' = x * sqrt(y)          →  return x * math.sqrt(y)
#   y' = x**2 - 3*y           →  return x**2 - 3*y
#   y' = -(y**1.5) + 1        →  return -(y**1.5) + 1
#   y' = y * math.tan(x)      →  return y * math.tan(x)
#   y' = x + y**2             →  return x + y**2
#   y' = 0.1*sqrt(y)+0.4*x**2 →  return 0.1*math.sqrt(y) + 0.4*x**2

def f(x, y):
    # ← CAMBIA ESTA LÍNEA con tu ecuación
    return x * math.sqrt(y)

ECUACION_STR = "y' = x·√y"          # Descripción de la ecuación (solo para el encabezado)
X0           = 1.0                   # Valor inicial de x
Y0           = 4.0                   # Condición inicial y(x0)
X_END        = 10.0                  # Punto a evaluar
H_LIST       = [0.1, 0.001, 0.00001] # Tamaños de paso

METODO       = "rk4"     # "euler" para Euler Mejorado | "rk4" para Runge-Kutta 4

# Primeras / últimas N iteraciones a mostrar (None = mostrar TODAS)
MOSTRAR_N    = None   # Cambia a None para ver todas las iteraciones
#              o pon un número, ej: MOSTRAR_N = 5

# ══════════════════════════════════════════════════════════════════════════════
#  ── MÉTODOS NUMÉRICOS ────────────────────────────────────────────────────────
# ══════════════════════════════════════════════════════════════════════════════

def euler_mejorado(x0, y0, x_end, h):
    """Euler Mejorado (Heun) — orden 2."""
    results = []
    x, y = x0, y0
    n_steps = round((x_end - x0) / h)
    results.append({"n": 0, "x": x, "y_star": None,
                    "k1": None, "k2": None, "k3": None, "k4": None, "y": y})
    for n in range(1, n_steps + 1):
        fx     = f(x, y)
        y_star = y + h * fx
        x_next = round(x + h, 10)
        y_next = y + (h / 2.0) * (fx + f(x_next, y_star))
        results.append({"n": n, "x": x_next, "y_star": y_star,
                        "k1": None, "k2": None, "k3": None, "k4": None, "y": y_next})
        x, y = x_next, y_next
    return results

def runge_kutta4(x0, y0, x_end, h):
    """Runge-Kutta de 4to orden."""
    results = []
    x, y = x0, y0
    n_steps = round((x_end - x0) / h)
    results.append({"n": 0, "x": x, "y_star": None,
                    "k1": None, "k2": None, "k3": None, "k4": None, "y": y})
    for n in range(1, n_steps + 1):
        k1 = h * f(x,         y)
        k2 = h * f(x + h/2,   y + k1/2)
        k3 = h * f(x + h/2,   y + k2/2)
        k4 = h * f(x + h,     y + k3)
        y_next = y + (k1 + 2*k2 + 2*k3 + k4) / 6.0
        x_next = round(x + h, 10)
        results.append({"n": n, "x": x_next, "y_star": None,
                        "k1": k1, "k2": k2, "k3": k3, "k4": k4, "y": y_next})
        x, y = x_next, y_next
    return results

# ══════════════════════════════════════════════════════════════════════════════
#  ── IMPRESIÓN DE TABLAS ──────────────────────────────────────────────────────
# ══════════════════════════════════════════════════════════════════════════════

def indices_a_mostrar(total, mostrar_n):
    """Devuelve el conjunto de índices a imprimir."""
    if mostrar_n is None:
        return set(range(total))
    first = list(range(min(mostrar_n + 1, total)))
    last  = list(range(max(total - mostrar_n, mostrar_n + 1), total))
    return set(first + last)

def print_euler(results, h, mostrar_n):
    total   = len(results)
    n_steps = total - 1
    metodo_nombre = "EULER MEJORADO (HEUN) — orden 2"

    print(f"\n{'='*76}")
    print(f"  {metodo_nombre}   h = {h}")
    print(f"  {ECUACION_STR},   y({X0}) = {Y0},   evaluar y({X_END})")
    print(f"  Pasos totales: {n_steps}  |  Mostrando: {'todas' if mostrar_n is None else f'primeras/últimas {mostrar_n}'}")
    print(f"{'='*76}")
    print(f"  {'n':>9}  {'xₙ':>10}  {'yₙ*':>13}  {'yₙ':>13}")
    print(f"  {'-'*9}  {'-'*10}  {'-'*13}  {'-'*13}")

    show_set = indices_a_mostrar(total, mostrar_n)
    ellipsis_printed = False

    for idx, row in enumerate(results):
        if idx in show_set:
            star = f"{'—':>13}" if row["y_star"] is None else f"{row['y_star']:>13.5f}"
            print(f"  {row['n']:>9}  {row['x']:>10.5f}  {star}  {row['y']:>13.5f}")
        else:
            if not ellipsis_printed:
                print(f"  {'...':>9}  {'...':>10}  {'...':>13}  {'...':>13}")
                ellipsis_printed = True

    print(f"{'='*76}")
    print(f"  >> y({X_END}) ≈ {results[-1]['y']:.5f}")
    print(f"{'='*76}\n")

def print_rk4(results, h, mostrar_n):
    total   = len(results)
    n_steps = total - 1
    metodo_nombre = "RUNGE-KUTTA 4to ORDEN"

    print(f"\n{'='*104}")
    print(f"  {metodo_nombre}   h = {h}")
    print(f"  {ECUACION_STR},   y({X0}) = {Y0},   evaluar y({X_END})")
    print(f"  Pasos totales: {n_steps}  |  Mostrando: {'todas' if mostrar_n is None else f'primeras/últimas {mostrar_n}'}")
    print(f"{'='*104}")
    print(f"  {'n':>9}  {'xₙ':>10}  {'k1':>12}  {'k2':>12}  {'k3':>12}  {'k4':>12}  {'yₙ':>13}")
    print(f"  {'-'*9}  {'-'*10}  {'-'*12}  {'-'*12}  {'-'*12}  {'-'*12}  {'-'*13}")

    show_set = indices_a_mostrar(total, mostrar_n)
    ellipsis_printed = False

    for idx, row in enumerate(results):
        if idx in show_set:
            if row["k1"] is None:
                print(f"  {row['n']:>9}  {row['x']:>10.5f}  {'—':>12}  {'—':>12}  {'—':>12}  {'—':>12}  {row['y']:>13.5f}")
            else:
                print(f"  {row['n']:>9}  {row['x']:>10.5f}  {row['k1']:>12.5f}  {row['k2']:>12.5f}  {row['k3']:>12.5f}  {row['k4']:>12.5f}  {row['y']:>13.5f}")
        else:
            if not ellipsis_printed:
                print(f"  {'...':>9}  {'...':>10}  {'...':>12}  {'...':>12}  {'...':>12}  {'...':>12}  {'...':>13}")
                ellipsis_printed = True

    print(f"{'='*104}")
    print(f"  >> y({X_END}) ≈ {results[-1]['y']:.5f}")
    print(f"{'='*104}\n")

# ══════════════════════════════════════════════════════════════════════════════
#  ── EJECUCIÓN PRINCIPAL ──────────────────────────────────────════════════════
# ══════════════════════════════════════════════════════════════════════════════

def main():
    metodo_lbl = METODO.strip().lower()

    print("\n" + "█"*76)
    print(f"  SOLUCIONADOR UNIVERSAL DE EDOs")
    print(f"  Ecuación : {ECUACION_STR}")
    print(f"  CI        : y({X0}) = {Y0}   →   evaluar y({X_END})")
    print(f"  Método    : {'Euler Mejorado (Heun)' if metodo_lbl == 'euler' else 'Runge-Kutta 4to orden'}")
    print(f"  Pasos h   : {H_LIST}")
    print(f"  Iterac.   : {'todas' if MOSTRAR_N is None else f'primeras/últimas {MOSTRAR_N}'}")
    print("█"*76)

    resumen = []

    for h in H_LIST:
        if metodo_lbl == "euler":
            res = euler_mejorado(X0, Y0, X_END, h)
            print_euler(res, h, MOSTRAR_N)
        elif metodo_lbl == "rk4":
            res = runge_kutta4(X0, Y0, X_END, h)
            print_rk4(res, h, MOSTRAR_N)
        else:
            print(f"  [ERROR] Método '{METODO}' no reconocido. Usa 'euler' o 'rk4'.")
            return
        resumen.append((h, res[-1]["y"]))

    # Tabla de convergencia
    print(f"\n{'─'*45}")
    print(f"  TABLA DE CONVERGENCIA — y({X_END})")
    print(f"{'─'*45}")
    print(f"  {'h':>12}   {'y(x_end)':>15}")
    print(f"  {'-'*12}   {'-'*15}")
    for h, val in resumen:
        print(f"  {h:>12g}   {val:>15.5f}")
    print(f"{'─'*45}\n")

if __name__ == "__main__":
    main()
