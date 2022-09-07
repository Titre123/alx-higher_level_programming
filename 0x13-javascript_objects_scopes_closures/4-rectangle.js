#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (((w = parseInt(w)) > 0) && ((h = parseInt(h)) > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    for (let i = 0; i < this.height; i++) {
      let Var = '';
      for (let j = 0; j < this.width; i++) {
        Var += 'X';
      }
      console.log(Var);
    }
  }

  rotate() {
    const width = this.width;
    const height = this.height;
    this.width = height;
    this.height = width;
  }

  double() {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
