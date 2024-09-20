#!/usr/bin/node

const axios = require('axios');

const fetchCharactersSequentially = async (urls) => {
    for (const url of urls) {
        try {
            const response = await axios.get(url);
            console.log(response.data.name);
        } catch (error) {
            console.error(error);
            throw error;
        }
    }
};

const fetchFilmCharacters = async (filmId) => {
    try {
        const response = await axios.get(`https://swapi-api.hbtn.io/api/films/${filmId}`);
        const characters = response.data.characters;
        await fetchCharactersSequentially(characters);
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
