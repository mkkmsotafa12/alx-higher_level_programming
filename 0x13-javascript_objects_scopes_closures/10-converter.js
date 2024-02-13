#!/usr/bin/node
exports.converter = function (base) {
  return function (inArgum) {
    return inArgum.toString(base)
  }
}
