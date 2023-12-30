"""
For an array containing 100 elements, provide the number of steps the following operations would take:

N = 100

1. Reading
    - one step because the index location is given

2. Searching for a value not contained within the array
    - N steps because the whole array must be searched

3. Insertion at the beginning of the array
    - N + 1 steps because all values in the array must be shifted to complete the insertion

4. Insertion at the end of the array
    - one step because no shifting is necessary

5. Deletion at the beginning of the array
    - N steps because the value must be deleted and all other values must be shifted

6. Deletion at the end of the array
    - one step because no shifting is necessary
"""
# Reading an array

pets = ["cat", "dog", "hamster", "fish"]

# read the whole array
print(pets)

#output --> ["cat", "dog", "hamster", "fish"]

# read a value at a specific index
print(pets[2])

# output --> hamster

# Searching for a value not contained within the array

new_pet = "snail"
if new_pet in pets:
    print(True)
else:
    print(False)

# output --> False

# Inserting a value into the beginning of an array

pets.insert(0, new_pet)
print(pets[0])
print(pets)

# output --> 
        # snail
        # ['snail', 'cat', 'dog', 'hamster', 'fish']

# Insert a value at the end of an array

pets.append("snake")
print(pets[-1])
print(pets)

# output -->
        # snake
        # ['snail', 'cat', 'dog', 'hamster', 'fish', 'snake']

# Deletion at the beginning of the array

# pop method
pets.pop(0)
print(pets)

# output --> ['cat', 'dog', 'hamster', 'fish', 'snake']

# slicing
pets = pets[1:]
print(pets)

# output --> ['dog', 'hamster', 'fish', 'snake']

# using del keyword
del pets[0]
print(pets)

# output --> ['hamster', 'fish', 'snake']

# Deletion at the end of the array

#pop method - when no index is given, it removes the last element
pets.pop()
print(pets)

# output --> ['hamster', 'fish']