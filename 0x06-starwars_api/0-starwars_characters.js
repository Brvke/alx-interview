#!/usr/bin/node
const request = require('request');
const { promisify } = require('util');

const film = process.argv[2];
const promisifiedReq = promisify(request);

(async () => {
  if (film >= 1 && film <= 7) {
    const res = await promisifiedReq(`https://swapi-api.alx-tools.com/api/films/${film}`);
    const reply = JSON.parse(res.body);
    const allRes = [];
    for (const characterLink of reply.characters) {
      allRes.push(promisifiedReq(characterLink));
    }
    const all = await Promise.all(allRes);
    for (const item of all) {
      const parsedItem = JSON.parse(item.body);
      console.log(parsedItem.name);
    }
  }
})();