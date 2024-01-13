/* 
Use Big O Notation to describe the time complexity of the following function
that sums up all the numbers from a given array.

Answer: O(N) because it takes as many steps as there are values in the array
*/

function arraySum(array) {
    let sum = 0;

    for (let i = 0; i < array.length; i++) {
        sum += array[i];
    }
    return sum;
}
