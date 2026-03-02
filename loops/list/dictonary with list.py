characters = [
    {"name": "goku", "power": "domain expansion", "show": "jjk"},
    {"name": "luffy", "power": "sun boy", "show": "one piece"},
    {"name": "saitama", "power": "one punch", "show": "opm"},
    {"name": "naruto", "power": "shadow clone", "show": "naruto"}
]

for character in characters:
    print(character["name"], character["power"], character["show"], sep=",")

    """
    1️⃣ List of Dictionaries

characters is a list.
Each element of the list is a dictionary.

Structure:

List
 ├── Dictionary 1
 ├── Dictionary 2
 ├── Dictionary 3
 └── Dictionary 4
2️⃣ Dictionary Structure

Each dictionary contains key–value pairs:

Example:

{"name": "goku", "power": "domain expansion", "show": "jjk"}

Keys:

"name"

"power"

"show"

3️⃣ Iteration Over List
for character in characters:

Each iteration assigns one dictionary to character.

4️⃣ Accessing Dictionary Values
character["name"]
character["power"]
character["show"]

This retrieves values using keys.

5️⃣ sep=","
print(..., sep=",")

Changes separator between printed values to a comma.
"""