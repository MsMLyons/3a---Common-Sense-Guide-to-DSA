/* 
Use Big O Notation to describe the time complexity of the following function that determines
whether a given year is a leap year.

Answer: O(1) because it takes 2 steps, regardless of the year
*/

function isLeapYear(year) {
    return (year % 100 === 0) ? (year % 400 === 0) : (year % 4 === 0);
}