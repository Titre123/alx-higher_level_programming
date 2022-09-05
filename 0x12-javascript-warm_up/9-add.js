#!/usr/bin/node
const args = process.argv;

function add (a, b) {
    /* This is function takes two arguments and
    return their sum
    Args-
        - a
        - b
    */
  console.log(Number(a) + Number(b));
}

add(args[2], args[3]);
