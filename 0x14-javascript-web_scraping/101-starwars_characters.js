#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});

function printCharacters(characters, index) {
  if (index >= characters.length) return;
  request(characters[index], (charError, charResponse, charBody) => {
    if (charError) {
      console.error(charError);
    } else {
      console.log(JSON.parse(charBody).name);
      printCharacters(characters, index + 1);
    }
  });
}
