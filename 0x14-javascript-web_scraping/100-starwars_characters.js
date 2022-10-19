#!/usr/bin/node

const request = require('request');

request('http://swapi.co/api/films/' + process.argv[2], function (error, response, body) {
    JSON.parse(body).characters.forEach(character => {
        request(url, function (error, response, body) {
    }
}
