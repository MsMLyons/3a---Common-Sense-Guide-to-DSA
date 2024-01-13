/* 
Use Big O Notation to describe the time complexity of the following function,
which accepts an array of strings and returns a new array that only contains 
the strings that start with the character 'a'.

Answer: O(N) because it's necessary to loop through the full array to find
the strings that begin with 'A'; for each item in the array, one step is taken
*/

function selectAString(array) {
    let newArray = [];

    for(let i = 0; i < array.length; i++) {
        if (array[i].startsWith("a")) {
            newArray.push(array[i]);
        }
    }
    return newArray;
}

