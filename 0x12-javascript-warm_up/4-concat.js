#!/usr/bin/node

const process = require('process'); // process global object
const args = process.argv;
if (args[2]) {
  console.log(`${args[2]}` + ' is ' + `${args[3]}`); // 3rd and 4th arg
} else if (args[2] && args[3]) {
  console.log(`${args[2]}` + ' is undefined');
} else {
  console.log('undefined is undefined');
}
