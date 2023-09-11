#!/usr/bin/node

const process = require('process');
const args = process.argv;
const x = args[2];
function factorial (x) {
  if (!x || x === 0) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}
console.log(factorial(x));
