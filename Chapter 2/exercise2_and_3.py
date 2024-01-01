"""
*Q2*
How many steps does it take to do a binary search to find the number
8 in the ordered array [2, 4, 6, 8, 10, 12, 13]?

Answer: 1 step (the value is found at index 3, in the exact middle of the array)
Code example, below.

*Q3*
How many steps does it take to perform a binary search on an array of 100,000 elements?

Answer: Divide 100,000 by 2 until reaching 1; 16 steps.
"""
def binary_search(array, value):
    lower = 0
    upper = len(my_array) - 1

    while lower <= upper:
        midpoint = (upper - lower) // 2
        value_at_midpoint = array[midpoint]

        if value == value_at_midpoint:
            return midpoint
        elif value < value_at_midpoint:
            upper = midpoint - 1
        elif value > value_at_midpoint:
                lower = midpoint + 1
        else:
            print("Value not found")
    
my_array = [2, 4, 6, 8, 10, 12, 13]
index_position = binary_search(my_array, 8)
print(f"The value 8 is found at index {index_position}")
