#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (((w = parseInt(w)) > 0) && ((h = parseInt(h)) > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let Var = '';
      for (let j = 0; j < this.width; j++) {
        Var += 'X';
      }
      console.log(Var);
    }
  }
}
module.exports = Rectangle;
