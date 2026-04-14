# Repositorio de EDOs Numéricas 🧮

Solución numérica de Ecuaciones Diferenciales Ordinarias (EDO) usando:
- **Euler - Euler Mejorado (Heun)** — método de orden 2
- **Runge-Kutta de 4to orden (RK4)** — método de orden 4

---

##  Estructura

```
/
├── Euler-Euler_mejorado/
│   ├── 01_euler_mejorado.py   → y' = 0.1√y + 0.4x²,  y(2)=4,  y(2+nh)
│   ├── 02_euler_mejorado.py           → y' = x√y,             y(1)=4,  y(10)
│   ├── 03_euler_mejorado.py        → y' = x²-3y,           y(0)=1,  y(15)
│   ├── 04_euler_mejorado.py     → y' = -y^(3/2)+1,      y(0)=10, y(20)
│   ├── 05_euler_mejorado.py            → y' = y·tan(x),        y(0)=1,  y(5)
│   └── 06_euler_mejorado.py           → y' = x+y²,            y(1)=0,  y(1.5)
│
├── RK4/
│   ├── 01_rk4.py                     → y' = x√y,             y(1)=4,  y(10)
│   ├── 02_rk4.py                  → y' = x²-3y,           y(0)=1,  y(15)
│   ├── 03_rk4.py               → y' = -y^(3/2)+1,      y(0)=10, y(20)
│   ├── 04_rk4.py                      → y' = y·tan(x),        y(0)=1,  y(5)
│   └── 05_rk4.py                     → y' = x+y²,            y(1)=0,  y(1.5)
│
└── Universal_Code.py                     ← ⭐ SOLVER GLOBAL CONFIGURABLE
```

---

##  Solver Universal — `Universal_Code.py`

Resuelve **cualquier EDO** simplemente editando la sección de configuración:

```python
# 1. Define tu ecuación
def f(x, y):
    return x * math.sqrt(y)        # ← cambia aquí

ECUACION_STR = "y' = x·√y"        # Descripción (encabezado)
X0           = 1.0                  # x inicial
Y0           = 4.0                  # y(x0) — condición inicial
X_END        = 10.0                 # punto a evaluar
H_LIST       = [0.1, 0.001, 0.00001]  # tamaños de paso

METODO       = "rk4"   # "euler" = Euler Mejorado | "rk4" = Runge-Kutta 4

MOSTRAR_N    = None    # None = TODAS las iteraciones | 5 = primeras/últimas 5
```

### Ejecución

```bash
python universal_ode_solver.py
```

### Ejemplos de ecuaciones

| EDO                        | Código `f(x,y)`                              |
|----------------------------|----------------------------------------------|
| y' = x√y                  | `return x * math.sqrt(y)`                    |
| y' = x² - 3y              | `return x**2 - 3*y`                          |
| y' = -y^(3/2) + 1         | `return -(y**1.5) + 1`                       |
| y' = y·tan(x)             | `return y * math.tan(x)`                     |
| y' = x + y²               | `return x + y**2`                            |
| y' = 0.1√y + 0.4x²       | `return 0.1*math.sqrt(y) + 0.4*x**2`        |
| y' = e^x - y              | `return math.exp(x) - y`                     |
| y' = sin(x) + y           | `return math.sin(x) + y`                     |

---

##  Tablas generadas

### Euler Mejorado
| n | xₙ | yₙ* | yₙ |
|---|----|----|-----|
| Iteración | x actual | Predictor | Corrector |

### Runge-Kutta 4
| n | xₙ | k1 | k2 | k3 | k4 | yₙ |
|---|----|----|----|----|----|----|
| Iteración | x actual | pendiente 1 | pendiente 2 | pendiente 3 | pendiente 4 | solución |

---

##  Requisitos

- Python 3.7+
- Solo librería estándar (`math`)
