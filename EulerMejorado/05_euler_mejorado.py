import math

def f(x, y):
    # y' - y*tan(x) = 0  =>  y' = y * tan(x)
    return y * math.tan(x)

def euler_mejorado(x0, y0, x_end, h):
    """
    Método de Euler Mejorado (Heun).
    Predictor:  y*_{n+1} = y_n + h * f(x_n, y_n)
    Corrector:  y_{n+1}  = y_n + h/2 * [f(x_n, y_n) + f(x_{n+1}, y*_{n+1})]
    """
    results = []
    x = x0
    y = y0
    n_steps = round((x_end - x0) / h)
    results.append((0, x, None, y))

    for n in range(1, n_steps + 1):
        fx     = f(x, y)
        y_star = y + h * fx
        x_next = round(x + h, 10)

        # Verificar singularidad en x_next (tan indefinida en π/2 + kπ)
        cos_val = math.cos(x_next)
        if abs(cos_val) < 1e-10:
            # Singularidad: detener integración
            print(f"  *** Singularidad en x = {x_next:.5f} (cos≈0). Integración detenida. ***")
            break

        y_next = y + (h / 2.0) * (fx + f(x_next, y_star))
        results.append((n, x_next, y_star, y_next))
        x = x_next
        y = y_next

    return results

def print_table(results, h, show_first=5, show_last=5):
    total   = len(results)
    n_steps = total - 1

    print(f"\n{'='*76}")
    print(f"  MÉTODO DE EULER MEJORADO (HEUN)   h = {h}")
    print(f"  y' = y·tan(x),   y(0) = 1,   evaluar y(5)")
    print(f"  Pasos realizados: {n_steps}")
    print(f"{'='*76}")
    print(f"  {'n':>9}  {'xₙ':>12}  {'yₙ*':>14}  {'yₙ':>14}")
    print(f"  {'-'*9}  {'-'*12}  {'-'*14}  {'-'*14}")

    first_idx = list(range(min(show_first + 1, total)))
    last_idx  = list(range(max(total - show_last, show_first + 1), total))
    show_set  = set(first_idx + last_idx)

    printed_ellipsis = False

    for idx, (n, x, y_star, y_n) in enumerate(results):
        if idx in show_set:
            star_str = f"{'—':>14}" if y_star is None else f"{y_star:>14.5f}"
            print(f"  {n:>9}  {x:>12.5f}  {star_str}  {y_n:>14.5f}")
        else:
            if not printed_ellipsis:
                print(f"  {'...':>9}  {'...':>12}  {'...':>14}  {'...':>14}")
                printed_ellipsis = True

    print(f"{'='*76}")
    last = results[-1]
    x_last = last[1]
    print(f"  >> y({x_last:.5f}) ≈ {last[3]:.5f}")

    # Solución exacta: y = 1/cos(x)  (solo si cos(x_last) != 0)
    cos_last = math.cos(x_last)
    if abs(cos_last) > 1e-10:
        y_exact = 1.0 / cos_last
        error = abs(last[3] - y_exact)
        print(f"  >> Solución exacta y = 1/cos(x):  y({x_last:.5f}) = {y_exact:.5f}")
        print(f"  >> Error absoluto: {error:.5e}")
    print(f"{'='*76}\n")

# ── Nota sobre singularidades ────────────────────────────────────────────────
# y' = y·tan(x)  →  solución exacta: y = C/cos(x)  con y(0)=1 → C=1
# tan(x) tiene singularidades en x = π/2 ≈ 1.5708, 3π/2 ≈ 4.7124, ...
# El dominio [0, 5] cruza DOS singularidades, por lo que el método
# numérico diverge al acercarse a ellas.
print("="*76)
print("  NOTA: y' = y·tan(x) tiene singularidades en x = π/2 ≈ 1.57080")
print("        y en x = 3π/2 ≈ 4.71239 dentro del dominio [0, 5].")
print("        El método se detendrá o divergirá al aproximarse a ellas.")
print("="*76)

x0, y0, x_end = 0.0, 1.0, 5.0

for h in [0.1, 0.001, 0.00001]:
    try:
        res = euler_mejorado(x0, y0, x_end, h)
        print_table(res, h)
    except Exception as e:
        print(f"\n  [h={h}] Error durante la integración: {e}\n")
