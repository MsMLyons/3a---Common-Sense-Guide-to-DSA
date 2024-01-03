def bubble_sort(list):
    # keep track of the unsorted rightmost index of the array
    unsorted_until_index = len(list) - 1
    # track whether the array is fully sorted
    sorted = False

    # loop runs as long as the array is not sorted
    while not sorted:
        # assume the array is sorted until a swap is made
        # remains true if a full loop is made without a swap
        sorted = True
        # for each value in the unsorted array:
        for i in range(unsorted_until_index):
            # compare adjacent values in the array
            if list[i] > list[i+1]:
                # swap the order of values
                list[i], list[i+1] = list[i+1], list[i]
                # turn sorted back to false when a swap is made
                sorted = False
        # decrement the index value by one each passthrough
        unsorted_until_index -= 1
    # return the list/array once sorted
    return list

print(bubble_sort([65, 55, 45, 35, 25, 15, 10]))