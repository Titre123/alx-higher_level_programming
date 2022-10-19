#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (err, response, body) =>{
    console.log("code:", response && response.statusCode);
});
