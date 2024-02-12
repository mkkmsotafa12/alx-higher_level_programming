#!/usr/bin/node

// this line for argument can’t be converted to an integer.

if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size')
} else {
const size = parseInt(process.argv[2])

// Convert the command-line argument to an integer

for (let i = 0; i < size; i++)
// Loop through rows based on the "size"
console.log("X".repeat(size))
// print all output
