 05/02/2026

# Matrix Calculator using NumPy:-

!pip install rich


import numpy as np
from rich import print

def input_matrix(name):
    print(f"\n[bold cyan]Enter Matrix {name}[/bold cyan]")
    rows = int(input("Rows: "))
    cols = int(input("Columns: "))

    matrix = []
    for i in range(rows):
        text = input("Row: ")        # "1 2 3"
        parts = text.split()         # ['1','2','3']
        nums = map(float, parts)     # 1.0,2.0,3.0
        row = list(nums)             # [1.0,2.0,3.0]

        matrix.append(row)

    return np.array(matrix)


A = input_matrix("A")
B = input_matrix("B")

print("\n[bold yellow]Choose Operation[/bold yellow]")
print("1. Addition")
print("2. Multiplication")
print("3. Transpose A")
print("4. Determinant A")
print("5. Inverse A")

choice = int(input("Enter choice: "))

if choice == 1:
    result = A + B
    print("\n[green]A + B =[/green]\n", result)

elif choice == 2:
    result = A @ B
    print("\n[green]A × B =[/green]\n", result)

elif choice == 3:
    print("\n[green]Transpose of A =[/green]\n", A.T)

elif choice == 4:
    print("\n[green]Determinant of A =[/green]", np.linalg.det(A))

elif choice == 5:
    print("\n[green]Inverse of A =[/green]\n", np.linalg.inv(A))

else:
    print("[red]Invalid choice[/red]")


x = "1 2 3"
x.split()
print(x.split())

def fun():
  x = [1.0,2.0,3.0]
  return np.array(x)
fun()

a = "234"
b=map(int,a)
print(type(b))
