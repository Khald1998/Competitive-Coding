'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'dayOfProgrammer' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts INTEGER year as parameter.
 */

function dayOfProgrammer(year) {
    // The day of the programmer is the 256th day of the year.
    // For the Julian calendar (years 1700-1917 in Russia), leap years are divisible by 4.
    // For the Gregorian calendar (years 1919 onwards in Russia), leap years are either
    // divisible by 400 or divisible by 4 but not by 100.

    // Special case: In 1918, Russia switched from the Julian to the Gregorian calendar,
    // resulting in February having less days. The 256th day in this year is the 26th of September.
    if (year === 1918) {
        return '26.09.' + year;
    }

    // Check if the year is a leap year in the Julian calendar (before 1918)
    // or in the Gregorian calendar (after 1918)
    let isLeapYear = (year < 1918 && year % 4 === 0) || 
                     (year > 1918 && (year % 400 === 0 || (year % 4 === 0 && year % 100 !== 0)));

    // If it's a leap year, the 256th day is September 12th
    // If it's not a leap year, the 256th day is September 13th
    let day = isLeapYear ? '12.09.' : '13.09.';
    return day + year;

}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const year = parseInt(readLine().trim(), 10);

    const result = dayOfProgrammer(year);

    ws.write(result + '\n');

    ws.end();
}
