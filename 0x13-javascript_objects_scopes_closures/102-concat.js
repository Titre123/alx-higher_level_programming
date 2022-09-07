#!/usr/bin/node

const fs = require('fs');

const contentInA = fs.readFileSync(process.argv[2], 'utf8', function (err, result) { if (err) console.log('error', err); });
const contentInB = fs.readFileSync(process.argv[3], 'utf8', function (err, result) { if (err) console.log('error', err); });

const contentInC = contentInA.concat(contentInB);

fs.writeFile(process.argv[4], contentInC, 'utf8', function (err, result) { if (err) console.log('error', err); });
