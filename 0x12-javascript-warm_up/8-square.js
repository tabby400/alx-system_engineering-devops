#!/usr/bin/node

const process = require('process');
const args = process.argv;

if (!args[2] || isNaN(args[2])) { // if missing or not valid no
  console.log('Missing size');
} else {
  for (let p = 0; p < args[2]; p++) {
    console.log('X'.repeat(args[2])); // first arg
  }
}
