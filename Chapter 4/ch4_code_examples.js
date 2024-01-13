/* 
Find and remove duplicate values from an array 
Time complexity O(N^2) due to nested loops used for comparison of array values
*/

function hasDuplicateValue(array) {
    for(let i = 0; i < array.length; i++) {
        for(let j = 0; j < array.length; j++) {
            if (i !== j && array[i] === array[j]) {
                return true;
            }
        }
    }
    return false;
}

// track the algorithm's number of steps

function hasDuplicateValue(array) {
    let steps = 0; // initialize count of steps
    for (let i = 0; i < array.length; i++) {
        for (let j = 0; j < array.length; j++) {
            steps++; // increment step count
            if (i !== j && array[i] === array[j]) {
                return true;
            }
        }
    }
    console.log(steps);
    return false;
}

/* 
Find and remove duplicate values from an array 
Time complexity O(N) 
- use an empty array to store and track the index of array values
- N comparisons for N elements
- one disadvantage --> memory consumption is greater with this algorithm
*/

function hasDuplicates(array) {
    let existingNumbers = [];
    for (let i = 0; i < array.length; i++) {
        if (existingNumbers[array[i]] === 1) {
            return true;
        } else {
            existingNumbers[array[i]] = 1;
        }
    }
    return false;
}

// track the algorithm's number of steps

function hasDuplicates(array) {
    let steps = 0;
    let existingNumbers = [];
    for (let i = 0; i < array.length; i++) {
        steps++;
        if (existingNumbers[array[i]] === 1) {
        return true;
        } else {
        existingNumbers[array[i]] = 1;
        }
    }
    console.log(steps)
    return false;
}


