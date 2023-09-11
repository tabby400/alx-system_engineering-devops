#!/usr/bin/node

const process = require('process');
const args = process.argv;
if (args.length === 2) { // path to executable and script itself
  console.log('No argument');
} else if (args.length < 4) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
