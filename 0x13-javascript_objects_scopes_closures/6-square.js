#!/usr/bin/node
const Square_ = require('./5-square');

class Square extends Square_ { // base class
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    const rw = c.repeat(this.width);
    for (let p = 0; p < this.height; p++) {
      console.log(rw);
    }
  }
}

module.exports = Square; // is accessible
