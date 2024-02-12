#!/usr/bin/node

let tmp
let value
if (process.argv.length <= 3) {
	console.log(0)
} else {
tmp = parseInt(process.argv[2])
for (let i = 2; i < process.argv.length; i++) {
if (parseInt(process.argv[i]) > tmp) {
      tmp = parseInt(process.argv[i]);
}
}
if (tmp !== parseInt(process.argv[2])) {
value = parseInt(process.argv[2]);
} else {
value = parseInt(process.argv[3]);
}
for (let i = 2; i < process.argv.length; i++) {
  if (parseInt(process.argv[i]) > value && parseInt(process.argv[i]) !== tmp) {
    value = parseInt(process.argv[i]);
}
}
console.log(value);
}
