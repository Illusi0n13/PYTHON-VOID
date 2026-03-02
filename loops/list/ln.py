character=['goku', 'gojo', 'saitama', 'naruto']
for i in range(len(character)):
    print(i+1, character[i])
"""
1️⃣ List Initialization

A list named character is created with 4 elements.

2️⃣ len(character)

Returns the total number of elements in the list.
Here:

len(character) → 4
3️⃣ range(len(character))

Creates a sequence:

0, 1, 2, 3

These are valid index positions.

4️⃣ Index-Based Iteration

i represents the index of each element.

So during iteration:

i	character[i]
0	goku
1	gojo
2	saitama
3	naruto
5️⃣ i + 1

Used to print numbering starting from 1 instead of 0.
"""