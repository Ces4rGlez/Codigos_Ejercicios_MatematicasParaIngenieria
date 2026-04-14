import math

def f(x, y):
    # y' - y*tan(x) = 0  =>  y' = y * tan(x)
    return y * math.tan(x)

def euler_basico(x0, y0, x_end, h):
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

    # Solución exacta: y = 1/cos(x)
    last_x = results[-1][1]
    cos_val = math.cos(last_x)
    y_exact = 1.0 / cos_val if abs(cos_val) > 1e-10 else float('inf')
    y_num   = results[-1][6]

    print(f"\n{'='*102}")
    print(f"  MÉTODO EULER BÁSICO (ORDEN 1)   h = {h}")
    print(f"  y' = y·tan(x),   y(0) = 1,   evaluar y(5)")
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
    print(f"  >> y(5) numérico  ≈ {y_num:.5f}")
    print(f"  >> y(5) exacto      = {y_exact:.5f}   [y = 1/cos(x)]")
    print(f"  >> Error absoluto   = {abs(y_num - y_exact):.2e}")
    print(f"{'='*102}\n")

# ── Advertencia sobre singularidades ─────────────────────────────────────────
print("="*102)
print("  NOTA: y' = y·tan(x) tiene singularidades en x = π/2 ≈ 1.57080 y x = 3π/2 ≈ 4.71239")
print("        dentro del dominio [0, 5]. El método numérico 'cruza' la singularidad con")
print("        errores que dependen del tamaño de paso h.")
print("="*102)

x0, y0, x_end = 0.0, 1.0, 5.0

for h in [0.1, 0.001, 0.00001]:
    res = euler_basico(x0, y0, x_end, h)
    print_table(res, h, show=3)

