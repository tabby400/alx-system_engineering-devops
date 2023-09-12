#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let p = 0; p < this.height; p++) {
      console.log('X'.repeat(this.width)); // rec printed withX
    }
  }
}

module.exports = Rectangle; // can be accessed
