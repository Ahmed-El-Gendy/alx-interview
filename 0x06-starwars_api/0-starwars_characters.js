#!/usr/bin/node

const axios = require('axios');

const fetchCharactersSequentially = async (arr, idx) => {
    if (idx === arr.length) {
        return;
    }
    try {
        const response = await axios.get(arr[idx]);
        console.log(response.data.name);
        fetchCharactersSequentially(arr, idx + 1);
    } catch (error) {
        console.error(error);
    }
};

axios.get(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`)
    .then(response => {
        const characters = response.data.characters;
        fetchCharactersSequentially(characters, 0);
    })
    .catch(error => {
        console.error(error);
    });
