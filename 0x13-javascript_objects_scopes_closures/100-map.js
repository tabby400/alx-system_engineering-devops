#!/usr/bin/node

const { list } = require('./100-data'); // module used

const newarr = list.map((value, index) => value * index);
console.log(list);
console.log(newarr); // value * index
