#!/usr/bin/node

const request = require('request');
const fs = require('fs');

let content;
request(process.argv[2], (err, res, body) => {
    fs.writeFile(process.argv[3], body, 'utf-8', (err) => {
    if (err) console.log(err);
   });
});
