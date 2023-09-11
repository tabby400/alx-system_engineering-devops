#!/usr/bin/node

const process = require('process');
const args = process.argv;
const arr = [];

if (!args[2] || args.length < 4) {
  console.log(0);
} else {
  for (let p = 2; p < args.length; p++) {
    arr.push(args[p]);
  }
  arr.sort(function (a, b) { return a - b; });
  console.log(arr.slice(-2)[0]);
}
