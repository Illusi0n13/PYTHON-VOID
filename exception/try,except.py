try:
    x=int(input('what is x?'))
          
except ValueError:
    print("x is not an integer")

else:
    print(f'x is {x}')

"""
1️⃣ try Block
x = int(input('what is x?'))

Takes input from the user.

Attempts to convert it into an integer.

If the conversion fails, Python raises a ValueError.

2️⃣ except ValueError
except ValueError:
    print("x is not an integer")

Executes when the user enters something that cannot be converted to an integer.

Prevents the program from crashing.

Example input:

abc

Output:

x is not an integer
3️⃣ else Block
else:
    print(f'x is {x}')

Runs only if no exception occurred in the try block.

Example input:

5

Output:

x is 5
"""