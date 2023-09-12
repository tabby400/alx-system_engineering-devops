#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle { // inheritance
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square; // can be used in other files
