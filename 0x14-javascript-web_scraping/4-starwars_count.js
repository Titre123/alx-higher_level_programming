#!/usr/bin/node

const request = require('request');
const urlWed = 'https://swapi-api.hbtn.io/api/people/18/';
const urlWed2 = 'http://swapi.co/api/people/18/';
const url = process.argv[2];
let wedFilms = 0;
request(url, (err, res, body) => {
  if (err) console.error('error:', err);
  const films = JSON.parse(body).results;
  for (const film of films) {
    const characters = film.characters;
    for (const character of characters) {
      if (character === urlWed || character === urlWed2) {
        wedFilms += 1;
      }
    }
  }
  console.log(wedFilms);
});
