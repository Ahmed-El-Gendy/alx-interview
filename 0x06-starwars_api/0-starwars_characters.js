#!/usr/bin/node

const request = require('request');

const fetchCharactersSequentially = (arr, idx) => {
  if (idx === arr.length) {
    return;
  }
  request(arr[idx], (err, response, body) => {
    if (err) {
      throw err;
    } else {
      console.log(JSON.parse(body).name);
      fetchCharactersSequentially(arr, idx + 1);
    }
  });
};

request(
    `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
    (err, response, body) => {
      if (err) {
        throw err;
      } else {
        const characters = JSON.parse(body).characters;
        fetchCharactersSequentially(characters, 0);
      }
    }
);
