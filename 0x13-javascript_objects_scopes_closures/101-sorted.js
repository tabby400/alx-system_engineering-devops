#!/usr/bin/node

const dict = require('./101-data').dict; // has what is to be transformed
const Dictnew = {}; // stores the changes key value pairs
for (const key in dict) {
  if (Dictnew[dict[key]] === undefined) {
    Dictnew[dict[key]] = [key];
  } else {
    Dictnew[dict[key]].push(key);
  }
}

console.log(Dictnew);
