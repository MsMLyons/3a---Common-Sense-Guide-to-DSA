def linear_search(array, search_value)
    # iterate through each element in the array
    array.each_with_index do |element, index|
        # return the index of the value if found
        if element == search_value
            return index
        # if element greater than searched value is reached, exit the loop
        elsif element > search_value
            break        
        end
    end
    # return nil if the value does not exist in the array
    return nil
end 
# call the function
p linear_search([3, 17, 75, 80, 202], 22)

def binary_search(array, search_value)
    # establish lower and upper bounds of the value search
    # lower bound is the first value in the array
    # upper bound is the last value in the array
    lower_bound = 0
    upper_bound = array.length - 1
    # loop through the array to find the midpoint between the lower and upper bounds
    while lower_bound <= upper_bound do
        # calculation to find the midpoint
        midpoint = (upper_bound - lower_bound) / 2
        # check the value at midpoint
        value_at_midpoint = array[midpoint]
        # if the midpoint value is the same as the search value, end the search
        if search_value == value_at_midpoint
            return midpoint
        # change the midpoint values based on whether it's necessary to guess higher or lower
        elsif search_value < value_at_midpoint
            upper_bound = midpoint - 1
        elsif search_value > value_at_midpoint
            lower_bound = midpoint + 1        
        end
    end
    # if the lower and upper bounds equal each other, then the value is not in the array
    return nil
end
