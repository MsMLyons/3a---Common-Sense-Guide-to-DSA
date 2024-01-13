import math 

# Exercise 1 - function to determine if a year is a Leap year

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"The year {year} is a leap year")
    else:
        print(f"The year {year} is not a leap year")

is_leap_year(2024)

# Exercise 2 - function to sum the values in an array

def sum_array(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    return sum

my_array = [1, 2, 3, 4]

print(sum_array(my_array))

# Exercise 3 - function to calculate the number of rice grains per chessboard square
# calculates the square you'll need to place a certain number of rice grains

def chessboard_space(num_grains):
    chessboard_spaces = 1
    placed_grains = 1

    while placed_grains < num_grains:
        placed_grains *= 2
        chessboard_spaces +=1

    return chessboard_spaces

print(chessboard_space(65))

# Exercise 4 - function to create new array of strings

def select_strings_that_begin_with_A(array):
    a_string_array = []
    beginning_char = 'A'

    for i in range(len(array)):
        if array[i][0].lower() == beginning_char.lower():
            a_string_array.append(array[i])
    return a_string_array

my_array = ['A good guide to guide dogs', 
            'Hotel California', 
            'Pumpkin pie is my least favorite',             
            'Happy is as happy does', 
            'A cute little puppy wagged its tail at me', 
            'There\'s a cute cat in the window', 
            'Amarillo is a nice name for a dog'] 

print(select_strings_that_begin_with_A(my_array))

# Exercise 5 - function to calculate median of an ordered array

def find_median(array):
    middle = math.floor(len(array) / 2)

    if len(array) % 2 == 0:
        return (array[middle -1] + array[middle]) / 2
    else:
        return array[middle]
    
new_array = [23, 31, 44, 56, 67, 78, 99, 102, 115]
print(find_median(new_array))