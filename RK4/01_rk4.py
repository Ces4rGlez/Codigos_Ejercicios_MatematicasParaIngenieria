import math

def f(x, y):
    return x * math.sqrt(y)

def runge_kutta4(x0, y0, x_end, h):
    """
    Método Runge-Kutta de 4to orden.
    k1 = h * f(x_n,        y_n)
    k2 = h * f(x_n + h/2,  y_n + k1/2)
    k3 = h * f(x_n + h/2,  y_n + k2/2)
    k4 = h * f(x_n + h,    y_n + k3)
    y_{n+1} = y_n + (1/6)(k1 + 2k2 + 2k3 + k4)
    """
    results = []
    x = x0
    y = y0
    n_steps = round((x_end - x0) / h)
    # iteración 0: sin k's todavía
    results.append((0, x, None, None, None, None, y))

    for n in range(1, n_steps + 1):
        k1 = h * f(x,           y)
        k2 = h * f(x + h/2,     y + k1/2)
        k3 = h * f(x + h/2,     y + k2/2)
        k4 = h * f(x + h,       y + k3)
        y_next = y + (k1 + 2*k2 + 2*k3 + k4) / 6.0
        x_next = round(x + h, 10)
        results.append((n, x_next, k1, k2, k3, k4, y_next))
        x = x_next
        y = y_next

    return results

def print_table(results, h, show=4):
    total   = len(results)
    n_steps = total - 1

    print(f"\n{'='*100}")
    print(f"  RUNGE-KUTTA 4to ORDEN   h = {h}")
    print(f"  y' = x·√y,   y(1) = 4,   evaluar y(10)")
    print(f"  Pasos totales: {n_steps}")
    print(f"{'='*100}")
    print(f"  {'n':>9}  {'xₙ':>10}  {'k1':>12}  {'k2':>12}  {'k3':>12}  {'k4':>12}  {'yₙ':>13}")
    print(f"  {'-'*9}  {'-'*10}  {'-'*12}  {'-'*12}  {'-'*12}  {'-'*12}  {'-'*13}")

    # índices a mostrar: primeras 'show' iteraciones (0..show) y últimas 'show'
    first_idx = list(range(min(show + 1, total)))
    last_idx  = list(range(max(total - show, show + 1), total))
    show_set  = set(first_idx + last_idx)

    printed_ellipsis = False

    for idx, (n, x, k1, k2, k3, k4, y_n) in enumerate(results):
        if idx in show_set:
            if k1 is None:
                print(f"  {n:>9}  {x:>10.5f}  {'—':>12}  {'—':>12}  {'—':>12}  {'—':>12}  {y_n:>13.5f}")
            else:
                print(f"  {n:>9}  {x:>10.5f}  {k1:>12.5f}  {k2:>12.5f}  {k3:>12.5f}  {k4:>12.5f}  {y_n:>13.5f}")
        else:
            if not printed_ellipsis:
                print(f"  {'...':>9}  {'...':>10}  {'...':>12}  {'...':>12}  {'...':>12}  {'...':>12}  {'...':>13}")
                printed_ellipsis = True

    print(f"{'='*100}")
    last = results[-1]
    print(f"  >> y(10) ≈ {last[6]:.5f}")
    print(f"{'='*100}\n")

# Condiciones
x0, y0, x_end = 1.0, 4.0, 10.0

for h in [0.1, 0.001, 0.00001]:
    res = runge_kutta4(x0, y0, x_end, h)
    print_table(res, h, show=4)
