""" 
The following function finds the greatest single number within an array, but
has an efficiency of O(N^2). Rewrite the function so that its efficiency 
increases to O(N).
"""

def greatest_number(array):

    for i in array:
        steps += 1
        is_i_greatest = True
        

        for j in array:
            steps += 1
            if j > i:
                is_i_greatest = False
            

        if is_i_greatest:
            return i               
        
my_array = [8, 2, 17, 99, 0, 23]
print(greatest_number(my_array))


# Answer:

def greater_number(array):    
    greatest_number = array[0]
    for i in array:
        steps += 1
        if i > greatest_number:
            greatest_number = i
        
    return greatest_number
    
new_array = [9, 1, 16, 100, 22, 3]
print(greatest_number(new_array))
