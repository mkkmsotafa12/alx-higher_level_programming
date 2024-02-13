#!/usr/bin/node
const Sq = require('./5-square.js');
class Square extends Sq {
  charPrint (c) {
    let val = '';
    for (let i = 0; i < this.width; i++) {
      if (c == null) {
        val += 'X'
      } else {
        val += c
      }
    }
    for (let i = 0; i < this.height; i++) {
      console.log(val)
    }
  }
}
module.exports = val
