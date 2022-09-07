#!/usr/bin/node

const dict = require('./101-data').dict;

const values = Object.entries(dict).reduce((acc, [key, value]) => {
  acc[value] = acc[value] ? [...acc[value], key] : [key];
  return acc;
}, {});
console.log(values);
