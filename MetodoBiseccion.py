import sympy as sp


def f(x, expr):
    # Evalúa la expresión dada en x.
    return expr.evalf(subs={symbol: x})


def bisection_method(expr, a, b, tolerance):
    # Aplica el método de bisección para encontrar la raíz y cuenta las iteraciones.
    if f(a, expr) * f(b, expr) >= 0:
        print(
            "\nNo se puede aplicar el método de bisección, no hay cambio de signo."
        )
        print(f"\nF(a): {f(a, expr)}\n" + f"F(b): {f(b, expr)}")
        return None, 0

    counter = 0  # Contador de iteraciones
    while True:
        xm = (a + b) / 2
        
        if abs(f(xm, expr)) < tolerance:
            return xm, counter

        if f(xm, expr) * f(a, expr) < 0:
            b = xm
        else:
            a = xm

        # Condición de escape: f(xm) < error.
        if abs (f((b - a) / 2, expr)) < tolerance:
            break
            
        counter += 1
    return (a + b) / 2, counter


# Definimos la variable simbólica
symbol = sp.symbols('x')

# Solicitar la entrada del usuario
print("Ingresa la ecuación en términos de x (por ejemplo, x**2 - 4):")
equation = input("Ecuación: ")
expr = sp.sympify(equation)

a = float(input("\nIngrese el límite inferior (a): "))
b = float(input("Ingrese el límite superior (b): "))
tolerance = float(input("Ingrese el error: "))

# Ejecutamos el método de bisección
raiz, iteraciones = bisection_method(expr, a, b, tolerance)

if raiz is not None:
    print(f"\nLa raíz encontrada es: {raiz}")
    print(f"f(raíz) = {abs(f(raiz, expr))}")
    print(f"Número de iteraciones realizadas: {iteraciones}")