#!/usr/bin/node

const axios = require('axios');

const fetchCharactersSequentially = (arr, idx) => {
    if (idx === arr.length) {
        return;
    }
    request(arr[idx], (err, body) => {
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
    (err, body) => {
        if (err) {
            throw err;
        } else {
            const characters = JSON.parse(body).results;
            fetchCharactersSequentially(characters, 0);
        }
    }
);
