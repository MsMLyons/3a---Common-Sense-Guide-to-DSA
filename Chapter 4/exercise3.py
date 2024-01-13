"""
Use Big O Notation to describe the time complexity of the following
function. It finds the greatest product of any pair of two numbers
within a given array.

Answer: O(N^2) because there is a nested loop to compare the products
of the values
"""

def greatestProduct(array):
    greatest_product_so_far = array[0] * array[1]

    for i, iVal in enumerate(array):
        for j, jVal in enumerate(array):
            if i != j and iVal * jVal > greatest_product_so_far:
                greatest_product_so_far = iVal * jVal
    
    return greatest_product_so_far