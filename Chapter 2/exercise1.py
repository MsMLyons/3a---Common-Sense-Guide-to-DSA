""" 
How many steps does it take to do a linear search to find the number
8 in the ordered array [2, 4, 6, 8, 10, 12, 13]?

Answer: 4 steps (the value is found at index 3)
"""
def linear_search(array, value):
    for x in range(len(array)):    
        if array[x] == value:            
            return x
        else:
            if x > value:
                break
    return -1        

my_array = [2, 4, 6, 8, 10, 12, 13]
index_position = linear_search(my_array, 8)
print(f"The value 8 is found at index {index_position}")