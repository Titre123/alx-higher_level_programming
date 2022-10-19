#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (err, response, body) => {
  if (err) console.error('error:', err);
  console.log('code:', response && response.statusCode);
});
