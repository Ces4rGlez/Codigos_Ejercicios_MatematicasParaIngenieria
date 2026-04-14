import math

def f(x, y):
    return x**2 - 3*y

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
        fx  = f(x, y)
        y_star = y + h * fx
        x_next = round(x + h, 10)
        y_next = y + (h / 2.0) * (fx + f(x_next, y_star))
        results.append((n, x_next, y_star, y_next))
        x = x_next
        y = y_next

    return results

def print_table(results, h, show_first=5, show_last=5):
    total  = len(results)
    n_steps = total - 1

    print(f"\n{'='*76}")
    print(f"  MÉTODO DE EULER MEJORADO (HEUN)   h = {h}")
    print(f"  y' = x² - 3y,   y(0) = 1,   evaluar y(15)")
    print(f"  Pasos totales: {n_steps}")
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
    print(f"  >> y(15) ≈ {last[3]:.5f}")
    print(f"{'='*76}\n")

# Condiciones
x0, y0, x_end = 0.0, 1.0, 15.0

for h in [0.1, 0.001, 0.00001]:
    res = euler_mejorado(x0, y0, x_end, h)
    print_table(res, h)
