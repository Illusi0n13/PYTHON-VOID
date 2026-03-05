def main():
    print_square(4)

def print_square(size):
    for i in range(size):
        for j in range(size):
            print('#', end='')
            
        print()
main()    

"""
1️⃣ main() Function
def main():
    print_square(4)

The entry function of the program.

Calls print_square() with size 4.

2️⃣ Function with Parameter
def print_square(size):

Defines a function that prints a square.

size determines the height and width of the square.

3️⃣ Outer Loop (Rows)
for i in range(size):

Controls the number of rows.

Since size = 4, the loop runs 4 times.

4️⃣ Inner Loop (Columns)
for j in range(size):

Prints # 4 times per row.

5️⃣ print('#', end='')

end='' prevents a newline.

Keeps printing # on the same line.

6️⃣ print()

After finishing one row:

print()

Moves to the next line.
"""