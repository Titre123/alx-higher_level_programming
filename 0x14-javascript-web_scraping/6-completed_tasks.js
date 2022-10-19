#!/usr/bin/node

const request = require('request');

const completed = {};
request(process.argv[2], function (error, response, body) {
  if (error) console.error('error:', error);
  const allTodos = JSON.parse(body);
  for (const todo of allTodos) {
    if (todo.completed && completed[todo.userId]) {
      completed[todo.userId] += 1;
    } else if (todo.completed && !completed[todo.userId]) {
      completed[todo.userId] = 1;
    }
  }
  console.log(completed);
});
