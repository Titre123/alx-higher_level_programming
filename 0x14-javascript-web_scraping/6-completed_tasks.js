#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const completed = {};
request(process.argv[2], function (error, response, body) {
    const all_todos = JSON.parse(body);
    for (const todo of all_todos) {
        if  (todo['completed'] && completed[todo['userId']]) {
            completed[todo['userId']] += 1;
        }
        else if (todo['completed'] && !completed[todo['userId']]) {
            completed[todo['userId']] = 1;
        }
    }
    console.log(completed);
})
