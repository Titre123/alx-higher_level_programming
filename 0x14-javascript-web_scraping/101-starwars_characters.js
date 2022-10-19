#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
for (let no = 1; no < 10; no++) {
  request(url, function (error, response, body) {
    if (error) console.error('Error:', error);
    const x = JSON.parse(body).characters;
    const urlOp = 'https://swapi-api.hbtn.io/api/people/?page=' + no;
    request(urlOp, function (error, response, body) {
      if (error) console.error('Error:', error);
      const array = [];
      const y = JSON.parse(body).results;
      for (const char of x) {
        for (const person of y) {
          if (char === person.url) {
            array.push(person.name);
          }
        }
      }
      for (const i of array) {
        console.log(i);
      }
    });
  });
}
