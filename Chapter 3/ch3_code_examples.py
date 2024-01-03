# Big O = O(N)
# Example 1

things = ["apples", "cheese", "trees", "porcupines"]

for thing in things:
    print("Here's a thing: " + thing)

# Example 2
def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

# Both examples demonstrate O(N) efficiency because as the number or dataset increases,
# so do the number of steps necessary to complete each iteration