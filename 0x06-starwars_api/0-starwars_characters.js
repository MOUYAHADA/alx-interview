#!/usr/bin/node

const request = require('request');

const req = (array, i) => {
  if (i === array.length) return;
  request(array[i], (err, res, body) => {
    if (err) throw err;
    else {
      console.log(JSON.parse(body).name);
      req(array, i + 1);
    }
  });
};

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], (err, res, body) => {
  if (err) throw err;
  const characters = JSON.parse(body).characters;
  req(characters, 0);
});
