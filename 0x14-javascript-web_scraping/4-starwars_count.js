#!/usr/bin/node

const request = require('request');
const url_wed = "https://swapi-api.hbtn.io/api/people/18/";
const url = process.argv[2];
let wed_films = 0;
request(url, (err, res, body) => {
    const films = JSON.parse(body)['results'];
    for (const film of films) {
        const characters = film['characters'];
        for (const character of characters) {
            if (character == url_wed) {
                wed_films += 1;
            };
        };
    };
    console.log(wed_films);
});

