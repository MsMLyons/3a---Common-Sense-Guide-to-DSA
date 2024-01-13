/* 
Describe the time complexity in terms of Big O Notation for the following function,
which calculates the median from an ordered array.

Answer: O(1) because once the middle (median) value is determined, the operation is complete
*/

function median(array) {
    const middle = Math.floor(array.length / 2);

    if(array.length % 2 === 0) {
        return (array[middle - 1] + array[middle]) / 2;
    } else {
        return array[middle]
    }
}