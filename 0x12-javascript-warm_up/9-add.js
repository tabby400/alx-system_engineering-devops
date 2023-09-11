#!/usr/bin/node

const process = require('process');
const argv = process.argv;
const x = Number(argv[2]); // convert 3rd arg to number
const y = Number(argv[3]);
const add = (x, y) => x + y;

console.log(add(x, y));
