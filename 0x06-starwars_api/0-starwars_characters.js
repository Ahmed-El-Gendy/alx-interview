#!/usr/bin/node

const request = require('request');

function printCharacters(characters) {
    characters.forEach((url) => {
        request(url, (error, response, body) => {
            if (!error) {
                const character = JSON.parse(body);
                console.log(character.name);
            }
        });
    });
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
    if (error) {
        console.error(error);
        return;
    }

    const filmData = JSON.parse(body);
    const characters = filmData.characters;

    printCharacters(characters);
});
