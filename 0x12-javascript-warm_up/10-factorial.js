#!/usr/bin/node

// This line defines a recursive function named "factorial" that calculate
function factorial (n) {

// If "n" is negative, the function returns -1 to indicate an invalid input
if (n < 0) {
	return (-1)
}

// If "n" is 0 or not a number (NaN), the function returns 1
if (n === 0 || isNaN(n)) {
	return (1)
}

return (n * factorial(n - 1))
}

// If none of the above conditions apply, the function returns
// "factorial" function with "n - 1"

console.log(factorial(Number(process.argv[2])))
