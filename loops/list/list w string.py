character=['goku', 'gojo', 'saitama', 'naruto']
print(character[0])
print(character[1])
print(character[2])
print(character[3])

# OR for character in character:
#     print(character)

"""
1️⃣ List Initialization

A list named character is created containing four string elements.

2️⃣ Ordered Data Structure

Lists maintain insertion order, so elements remain in the sequence they were defined.

3️⃣ Zero-Based Indexing

Python lists start indexing from 0:

character[0] → first element

character[3] → fourth element

4️⃣ Index Access

Each print() statement accesses a specific element using its index.

5️⃣ Sequential Output

Each element is printed one after another on separate lines because print() adds a newline by default.

6️⃣ Fixed Access Method

The program accesses elements manually using hardcoded indices rather than dynamically.

7️⃣ Limitation

If the list size changes, additional print() statements must be added manually.
"""

"""
ANOTHER WAY TO PRINT ALL ELEMENTS IN THE LIST
character=['goku', 'gojo', 'saitama', 'naruto']
for character in character:
    print(character)

#2️⃣ Loop Iteration
for character in character:

This means:

Take each element from the list

Assign it to the loop variable character

Execute the block
"""