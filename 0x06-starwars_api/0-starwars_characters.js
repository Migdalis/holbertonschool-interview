#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, async function (err, resp, body) {
    if (err) {
        console.log(err);
    }
    const characters = JSON.parse(body).characters;
    characters.array.forEach(element => {
        await new Promise((resolve, reject) => {
            request(element, (err, resp, body) => {
                if (err) {
                    reject(err);
                }
                console.log(JSON.parse(body).name);
                resolve();
            });
        });
    });
});
