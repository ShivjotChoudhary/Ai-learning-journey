# **# Step 1: Install Numpy and Rich Library**

!pip install rich
!pip install numpy

# **Step 2: Import Libraries**

import numpy as np
from rich import print


# **Step 3: Create Function to Take Matrix Input**

def input_matrix(name):
    print(f"\n[bold cyan]Enter Matrix {name}[/bold cyan]")
    rows = int(input("Rows: "))
    cols = int(input("Columns: "))

    matrix = []
    for i in range(rows):
        text = input("Row: ")    # yeh "1 2 3"input lega
        parts = text.split()     # string ko break krega peices:-['1','2','3']
        nums = map(float, parts) # map()-string ko floatmein convert-1.0,2.0,3.0
        row = list(nums)         # store krega list mein[1.0,2.0,3.0]

        matrix.append(row)       #matrix[] mein add kr dega

    return np.array(matrix)      #uss matrix ka numpy array dega return

# **Step 4: Take Matrix A and B from User**

A = input_matrix("A")       #function ko call
B = input_matrix("B")


# **Step 5: Show Menu**

print("[bold yellow]Choose Operation[/bold yellow]\n")
print("1. Addition")
print("2. Multiplication")
print("3. Transpose A")
print("4. Determinant A")
print("5. Inverse A")

choice = int(input("Enter choice: ")) #choice mein store kr lega (int)value only


# **Step 6: Perform Operations Based on Choice**

if choice == 1:
    result = A + B
    print("\n[green]A + B =[/green]\n", result)

elif choice == 2:
    result = A @ B
    print("\n[green]A × B =[/green]\n", result)
# why @? yeh row x column kr deta hai and * = element by element krta hai

elif choice == 3:
    print("\n[green]Transpose of A =[/green]\n", A.T)

elif choice == 4:
    print("\n[green]Determinant of A =[/green]", np.linalg.det(A))
#.determinant ke liye .det() and .linalg (module) hai linear algebra k liye

elif choice == 5:
    print("\n[green]Inverse of A =[/green]\n", np.linalg.inv(A))

else:
    print("[red]Invalid choice[/red]")




                             
