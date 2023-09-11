#!/usr/bin/node

const process = require('process');
const args = process.argv;
if (!args[2]) { // cant convert to int
  console.log('Missing number of occurrences');
} else {
  for (let p = 0; p < args[2]; p++) { // times equal to 3rd arg
    console.log('C is fun');
  }
}
