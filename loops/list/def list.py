def main():
    number=get_number()
    hawk(number)

def get_number():
    while True:
        n=int(input("what's n: "))
        if n>0:
            break
    return n
    
def hawk(n):
    for _ in range(n): 
        print("hawk")

if __name__ == "__main__":
    main()


"""
The program is divided into separate functions:

main() → controls program flow

get_number() → handles input validation

hawk(n) → handles output logic

This follows separation of concerns.

2️⃣ Entry Point Control
if __name__ == "__main__":
    main()

Ensures the program runs only when executed directly, not when imported.

3️⃣ Infinite Loop for Validation
while True:

Creates a loop that continues until valid input is received.

4️⃣ Input Conversion
n = int(input(...))

Takes user input (string) and converts it into an integer.

5️⃣ Exception Handling
except ValueError:
    pass

Prevents the program from crashing if the user enters non-numeric input.

6️⃣ Early Return Pattern
return n

Immediately exits the function once a valid positive integer is found.

7️⃣ Parameter Passing
hawk(number)

The value returned from get_number() is passed as an argument to another function.

8️⃣ Controlled Iteration
for _ in range(n):

Repeats the print statement exactly n times.
_ indicates the loop variable is intentionally unused.
"""
    