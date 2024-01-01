/* 
Imagine you have a chessboard and put a single grain of rice on one square. On the
second square, you put 2 grains of rice, since that is double the amount of rice on
the previous square. On the third square, you put 4 grains. On the fourht square,
you put 8 grains, and on the fifth square, you put 16 grains, and so on.

The function that follows calculates the square you'll need to place a certain
number of rice grains. For example, for 16 grains, the function will return 5.

Use Big O Notation to describe the time complexity of this function.

Answer:

*/

function chessboardSpace(numberOfGrains) {
    let chessboardSpaces = 1;
    let placedGrains = 1;

    while (placedGrains < numberOfGrains) {
        placedGrains *= 2;
        chessboardSpaces += 1;
    }
    return chessboardSpaces;
}