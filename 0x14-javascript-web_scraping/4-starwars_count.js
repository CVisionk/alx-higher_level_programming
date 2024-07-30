#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;

    films.forEach(film => {
      film.characters.forEach(character => {
        if (character.includes('18')) {
          count++;
        }
      });
    });

    console.log(count);
  }
});
