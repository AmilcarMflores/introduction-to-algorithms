# Problem Description: Dado un número n, escribe un algoritmo para imprimir una pirámide de asteriscos con n niveles.

def print_pyramid(n):
  for i in range(n):
     # Imprimimos n - i - 1 espacios en blanco, 2 * i + 1 asteriscos y n - i - 1 espacios en blanco
    print(" " * (n - i - 1) + "*" * (2 * i + 1) + " " * (n - i - 1))
    
print_pyramid(5) 