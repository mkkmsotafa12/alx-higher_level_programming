#!/usr/bin/node

// This line defines a function named "add"

function add(a, b) {
const n = a + b
console.log(n)
}
add(Number(process.argv[2]), Number(process.argv[3]))
