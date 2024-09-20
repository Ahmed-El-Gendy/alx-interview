#!/usr/bin/node

const axios = require('axios');

const fetchCharacters = async (urls) => {
    try {
        for (let url of urls) {
            const response = await axios.get(url);
            console.log(response.data.name);
        }
    } catch (error) {
        console.error(error);
    }
};

const fetchFilmCharacters = async (filmId) => {
    try {
        const response = await axios.get(`https://swapi-api.hbtn.io/api/films/${filmId}`);
        const characters = response.data.characters;
        await fetchCharacters(characters);
    } catch (error) {
        console.error(error);
    }
};

const filmId = process.argv[2];
if (filmId) {
    fetchFilmCharacters(filmId);
} else {
    console.log('Please provide a film ID');
}
