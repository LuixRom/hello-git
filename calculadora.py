import re

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def evaluar_expresion(expresion):
    expresion = expresion.replace(" ", "")  # Eliminar espacios

    # Evaluar paréntesis primero
    while '(' in expresion:
        subexpr = re.search(r'\(([^()]+)\)', expresion)
        if subexpr:
            resultado = evaluar_expresion(subexpr.group(1))
            expresion = expresion.replace(subexpr.group(0), str(resultado))

    # Evaluar multiplicación y división
    while re.search(r'(\d+\.?\d*[\*/]-?\d+\.?\d*)', expresion):
        match = re.search(r'(\d+\.?\d*)([\*/])(-?\d+\.?\d*)', expresion)
        a, op, b = float(match.group(1)), match.group(2), float(match.group(3))
        if op == '*':
            resultado = multiplicacion(a, b)
        else:
            resultado = division(a, b)
        expresion = expresion.replace(match.group(0), str(resultado), 1)

    # Evaluar suma y resta
    while re.search(r'(-?\d+\.?\d*[\+-]-?\d+\.?\d*)', expresion):
        match = re.search(r'(-?\d+\.?\d*)([\+-])(-?\d+\.?\d*)', expresion)
        a, op, b = float(match.group(1)), match.group(2), float(match.group(3))
        if op == '+':
            resultado = suma(a, b)
        else:
            resultado = resta(a, b)
        expresion = expresion.replace(match.group(0), str(resultado), 1)

    return float(expresion)

def main():
    print("Bienvenido a la Calculadora CLI")
    print("Escribe una operación completa (ej: 2 + 2 * (3 - 1)) y presiona Enter para calcular")
    print("Usa 'c' para borrar la operación actual, o 'q' para salir")
    
    while True:
        entrada = input("> ")
        
        if entrada.lower() == 'q':
            print("¡Hasta luego!")
            break
        elif entrada.lower() == 'c':
            print("Operación borrada")
            continue
        
        try:
            resultado = evaluar_expresion(entrada)
            print(f"Resultado: {resultado}")
        except ValueError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"Error inesperado: {str(e)}")

if __name__ == "__main__":
    main()
