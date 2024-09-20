#!/usr/bin/node

const request = require('request');


function fetch(url) {
    return new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
            if (error) {
                return reject(error);
            }
            resolve(JSON.parse(body));
        });
    });
}


async function printCharacters(characters) {
    for (const url of characters) {
        try {
            const character = await fetch(url);
            console.log(character.name);
        } catch (error) {
            console.error(error);
        }
    }
}


async function main() {
    const movieId = process.argv[2];
    const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

    try {
        const filmData = await fetch(apiUrl);
        const characters = filmData.characters;
        await printCharacters(characters);
    } catch (error) {
        console.error(error);
    }
}

main();
