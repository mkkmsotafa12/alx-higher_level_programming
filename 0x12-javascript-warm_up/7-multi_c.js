#!/usr/bin/node

if (parseInt(process.argv[2])) {
let x = parseInt(process.argv[2])
  for (let i = 0; i < x; i++) {
    console.log("C is fun")
  }
} else {
	console.log("Missing number of occurrences")
}
