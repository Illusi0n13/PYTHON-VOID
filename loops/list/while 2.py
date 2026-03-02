while True:
    n=int(input("what's n: "))
    if n>0:
        break
for _ in range(n):
    print("meow")

""""
What This Code Actually Does

while True: → infinite loop

Ask user for n

If n > 0 → break immediately

The for loop is inside the while loop but outside the if

"""