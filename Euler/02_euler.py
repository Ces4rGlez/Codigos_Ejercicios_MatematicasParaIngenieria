import math

def f(x, y):
    return x**2 - 3*y

def euler_basico(x0, y0, x_end, h):
    """
    Método Euler Básico (Explícito) — orden 1.
    Δy = h * f(x_n, y_n)
    y_{n+1} = y_n + Δy
    """
    results = []
    x = x0
    y = y0
    n_steps = round((x_end - x0) / h)
    results.append((0, x, None, None, None, None, y))

    for n in range(1, n_steps + 1):
        dy = h * f(x, y)
        y_next = y + dy
        x_next = round(x + h, 10)
        results.append((n, x_next, dy, None, None, None, y_next))
        x = x_next
        y = y_next

    return results

def print_table(results, h, show=3):
    total   = len(results)
    n_steps = total - 1

    print(f"\n{'='*102}")
    print(f"  MÉTODO EULER BÁSICO (ORDEN 1)   h = {h}")
    print(f"  y' = x² - 3y,   y(0) = 1,   evaluar y(15)")
    print(f"  Pasos totales: {n_steps}")
    print(f"{'='*102}")
    print(f"  {'n':>9}  {'xₙ':>10}  {'Δy':>12}  {'—':>12}  {'—':>12}  {'—':>12}  {'yₙ':>13}")
    print(f"  {'-'*9}  {'-'*10}  {'-'*12}  {'-'*12}  {'-'*12}  {'-'*12}  {'-'*13}")

    first_idx = list(range(min(show + 1, total)))
    last_idx  = list(range(max(total - show, show + 1), total))
    show_set  = set(first_idx + last_idx)
    printed_ellipsis = False

    for idx, (n, x, dy, _, _, _, y_n) in enumerate(results):
        if idx in show_set:
            if dy is None:
                print(f"  {n:>9}  {x:>10.5f}  {'—':>12}  {'—':>12}  {'—':>12}  {'—':>12}  {y_n:>13.5f}")
            else:
                print(f"  {n:>9}  {x:>10.5f}  {dy:>12.5f}  {'—':>12}  {'—':>12}  {'—':>12}  {y_n:>13.5f}")
        else:
            if not printed_ellipsis:
                print(f"  {'...':>9}  {'...':>10}  {'...':>12}  {'...':>12}  {'...':>12}  {'...':>12}  {'...':>13}")
                printed_ellipsis = True

    print(f"{'='*102}")
    last = results[-1]
    print(f"  >> y(15) ≈ {last[6]:.5f}")
    print(f"{'='*102}\n")

x0, y0, x_end = 0.0, 1.0, 15.0

for h in [0.1, 0.001, 0.00001]:
    res = euler_basico(x0, y0, x_end, h)
    print_table(res, h, show=3)

