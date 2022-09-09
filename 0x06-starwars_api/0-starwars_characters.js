#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, async function (err, resp, body) {
    if (err) {
        console.log(err);
    }
    for (const character of JSON.parse(body).characters) {
        await new Promise((resolve, reject) => {
            request(character, (err, resp, body) => {
                if (err) {
                    reject(err);
                }
                console.log(JSON.parse(body).name);
                resolve();
            });
        });
    }
});
