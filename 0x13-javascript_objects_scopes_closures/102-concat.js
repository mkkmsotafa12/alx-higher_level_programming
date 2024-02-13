#!/usr/bin/node
const fs = require('fs')
const file_one = fs.readFileSync(process.argv[2])
const file_two = fs.readFileSync(process.argv[3])
fs.writeFileSync(process.argv[4], file_one + file_two, 'utf-8')
