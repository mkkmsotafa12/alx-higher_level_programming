#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDic = {}
for (const key in dict) {
  if (newDic[dict[key]] === undefined) {
    newDic[dict[key]] = [key]
  } else {
    newDic[dict[key]].push(key)
  }
}
console.log(newDic)
