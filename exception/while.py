def main():
    x=get_int()
    print(f'x is {x}')


def get_int():
    while True:
        try:
            return int(input('what is x?'))
        except ValueError:
            print("x is not an integer")
        else:
            return x
        
main()

"""
Points That Define This Code
1️⃣ main() Function

Acts as the entry point of the program.
It calls get_int() to obtain a valid integer and prints the result.

2️⃣ Function Call
x = get_int()

The program calls get_int() and stores the returned value in variable x.

3️⃣ Infinite Loop
while True:

Creates a loop that keeps running until a valid integer is entered.

4️⃣ Exception Handling
try:

Attempts to convert user input into an integer using int().

5️⃣ Error Handling
except ValueError:

Handles the error that occurs when the user enters a non-numeric value.

Example invalid input:

abc
6️⃣ Error Message
print("x is not an integer")

Displays a message informing the user that the input is invalid.

7️⃣ Returning Valid Input
return int(input(...))

If the input is a valid integer, the function returns the value to main().

8️⃣ Program Execution
main()

Starts the program by calling the main() function.

Output Example
what is x? abc
x is not an integer
what is x? 5
x is 5
"""

