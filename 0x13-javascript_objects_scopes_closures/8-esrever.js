#!/usr/bin/node
exports.esrever = function (list) {
  const List = []
  for (let i = 0; i < list.length; i++) {
    	List.push(list[list.length - 1 - i])
  }
  return List
}
