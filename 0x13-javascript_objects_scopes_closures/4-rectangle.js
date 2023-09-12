#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  rotate () {
    [this.height, this.width] = [this.width, this.height];
  } // exchanges the height and the width of rec

  double () {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  } // double the width and height

  print () {
    for (let p = 0; p < this.height; p++) {
      console.log('X'.repeat(this.width));
    } // print rec using X
  }
}

module.exports = Rectangle;
