"""
For an array-based set containing 100 elements, provide the number of steps the following operations would take:

N = 100

1. Reading
    - N steps because it requires looking at all elements

2. Searching for a value not contained within the set
    - N steps because the whole set must be searched

3. Insertion at the beginning of the set
    - 2N + 1 steps because all values in the set must be searched to avoid duplication
    - and then all elements must be shifted to complete the insertion if the element is unique
    * Note that sets are unordered, so the location of a value's insertion into a set is generally arbitrary

4. Insertion at the end of the set
    - N + 1 steps because all elements must be searched for duplicates before insertion can take place
    * Note that sets are unordered, so the location of a value's insertion into a set is generally arbitrary

5. Deletion at the beginning of the set
    - N steps because the value must be deleted and all other values must be shifted
    * Note that sets it's necessary to know the specific value at the beginning of the set to call it for deletion

6. Deletion at the end of the set
    - one step because no shifting is necessary
    * Note that sets it's necessary to know the specific value at the end of the set to call it for deletion
"""

# Reading a set

pets = {"fish", "baby shark", "hedgehog", "cat", "dog", "snake"}

# read the whole set
print(pets)

# output --> {'fish', 'snake', 'dog', 'hedgehog', 'cat', 'baby shark'}

# Search for value (not) in set

print("snake" in pets)
print("bernese mountain dog" in pets)
print("baby shark" not in pets)
print("hamster" not in pets)

# output --> 
        # True
        # False
        # False
        # True

# Insertion into a set (location will vary/be arbitrarily assigned)

pets.add("hamster")
print(pets)

# output --> {'hamster', 'hedgehog', 'fish', 'dog', 'cat', 'snake', 'baby shark'}

# Delete a value from a set

pets.remove("hedgehog")
print(pets)

# output --> {'fish', 'dog', 'snake', 'baby shark', 'cat', 'hamster'}