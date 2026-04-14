import math

def f(x, y):
    # y' = x + y^2
    return x + y**2

def runge_kutta4(x0, y0, x_end, h):
    results = []
    x = x0
    y = y0
    n_steps = round((x_end - x0) / h)
    results.append((0, x, None, None, None, None, y))

    for n in range(1, n_steps + 1):
        k1 = h * f(x,         y)
        k2 = h * f(x + h/2,   y + k1/2)
        k3 = h * f(x + h/2,   y + k2/2)
        k4 = h * f(x + h,     y + k3)
        y_next = y + (k1 + 2*k2 + 2*k3 + k4) / 6.0
        x_next = round(x + h, 10)
        results.append((n, x_next, k1, k2, k3, k4, y_next))
        x = x_next
        y = y_next

    return results

def print_table(results, h, show=3, show_all_limit=5):
    total   = len(results)
    n_steps = total - 1

    print(f"\n{'='*102}")
    print(f"  RUNGE-KUTTA 4to ORDEN   h = {h}")
    print(f"  y' = x + y²,   y(1) = 0,   evaluar y(1.5)")
    print(f"  Pasos totales: {n_steps}")
    print(f"{'='*102}")
    print(f"  {'n':>9}  {'xₙ':>10}  {'k1':>12}  {'k2':>12}  {'k3':>12}  {'k4':>12}  {'yₙ':>13}")
    print(f"  {'-'*9}  {'-'*10}  {'-'*12}  {'-'*12}  {'-'*12}  {'-'*12}  {'-'*13}")

    # Si hay pocos pasos, mostrar todo
    if total <= show_all_limit:
        show_set = set(range(total))
    else:
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

    print(f"{'='*102}")
    last = results[-1]
    print(f"  >> y(1.5) ≈ {last[6]:.5f}")
    print(f"{'='*102}\n")

x0, y0, x_end = 1.0, 0.0, 1.5

for h in [0.1, 0.001, 0.00001]:
    res = runge_kutta4(x0, y0, x_end, h)
    print_table(res, h, show=3, show_all_limit=7)
