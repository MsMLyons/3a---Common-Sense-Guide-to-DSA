""" 
How many steps does it take to count the number of a specific value in an array?

N steps because the whole array must be traversed to find each instance of the specific value
"""
# Different methods of finding the index of specific values in an array

# for loop
def get_cat_indices(pet, pets):
    indices = []
    for i in range(len(pets)):
        if pets[i] == pet:
            indices.append(i)
    return indices

pets = ["parrot", "dog", "hamster", "dog", "cat", "turtle", "cat", "horse", "cat", "snake", "cat", "hedgehog", "cat", "dog", "hamster", "cat", "parrot", "fish"]
pet = "cat"
cat_indices = get_cat_indices(pet, pets)
print(cat_indices)

# output --> [4, 6, 8, 10, 12, 15]

# list comprehension
def get_dog_indices(pet, pets):
    return [i for i in range(len(pets)) if pets[i] == pet]

pet = "dog"
dog_indices = get_dog_indices(pet, pets)
print(dog_indices)

# output --> [1, 3, 13]

# enumerate function
def get_turtle_indices(pet, pets):
    return [i for i, x in enumerate(pets) if x == pet]

pet = "turtle"
turtle_indices = get_turtle_indices(pet, pets)
print(turtle_indices)

# output --> [5]

# index method with while loop
def get_hamster_indices(pet, list):
    indices = []
    index = -1
    while True:
        try:
            index = list.index(pet, index + 1)
            indices.append(index)
        except ValueError:
            break
    return indices

pets = ["dog", "hamster", "turtle", "cat", "horse", "snake", "hedgehog", "cat", "dog", "hamster", "fish"]
pet = "hamster"
hamster_indices = get_hamster_indices(pet, pets)
print(hamster_indices)

# output --> [1, 9]