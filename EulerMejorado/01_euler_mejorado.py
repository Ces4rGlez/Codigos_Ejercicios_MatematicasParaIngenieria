import math

def f(x, y):
    return 0.1 * math.sqrt(y) + 0.4 * x**2

def euler_mejorado(x0, y0, h, n_steps):
    """
    Método de Euler Mejorado (Heun).
    y*_{n+1} = y_n + h * f(x_n, y_n)          <- predictor
    y_{n+1}  = y_n + h/2 * [f(x_n, y_n) + f(x_{n+1}, y*_{n+1})]  <- corrector
    Retorna lista de (n, x_n, y_star, y_n)
    """
    results = []
    x = x0
    y = y0
    # Iteración 0
    results.append((0, x, None, y))

    for n in range(1, n_steps + 1):
        y_star = y + h * f(x, y)
        x_next = x + h
        y_next = y + (h / 2) * (f(x, y) + f(x_next, y_star))
        results.append((n, x_next, y_star, y_next))
        x = x_next
        y = y_next

    return results

def print_table(results, h, show_first=5, show_last=5):
    total = len(results)
    print(f"\n{'='*72}")
    print(f"  MÉTODO DE EULER MEJORADO (HEUN)   h = {h}")
    print(f"  y' = 0.1·√y + 0.4x²,   y(2) = 4")
    print(f"{'='*72}")
    print(f"  {'n':>5}  {'xₙ':>10}  {'yₙ*':>13}  {'yₙ':>13}")
    print(f"  {'-'*5}  {'-'*10}  {'-'*13}  {'-'*13}")

    # Índices a mostrar
    first_indices = list(range(min(show_first + 1, total)))
    last_indices  = list(range(max(total - show_last, show_first + 1), total))

    shown = set()
    printed_ellipsis = False

    for idx, (n, x, y_star, y_n) in enumerate(results):
        if idx in first_indices or idx in last_indices:
            shown.add(idx)
            if y_star is None:
                star_str = f"{'—':>13}"
            else:
                star_str = f"{y_star:>13.5f}"
            print(f"  {n:>5}  {x:>10.5f}  {star_str}  {y_n:>13.5f}")
        else:
            if not printed_ellipsis:
                print(f"  {'...':>5}  {'...':>10}  {'...':>13}  {'...':>13}")
                printed_ellipsis = True

    print(f"{'='*72}\n")

# ── h = 0.1 ──────────────────────────────────────────────────────────────────
x0, y0 = 2.0, 4.0
h1 = 0.1
# Para que tenga sentido un rango, integramos hasta x = 3 (10 pasos)
n1 = 10
res1 = euler_mejorado(x0, y0, h1, n1)
print_table(res1, h1, show_first=5, show_last=5)

# ── h = 0.05 ─────────────────────────────────────────────────────────────────
h2 = 0.05
# Mismo dominio x ∈ [2, 3] → 20 pasos
n2 = 20
res2 = euler_mejorado(x0, y0, h2, n2)
print_table(res2, h2, show_first=5, show_last=5)
