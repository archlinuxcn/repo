#!/usr/bin/env node
const fs = require('fs');

const content = fs.readFileSync('./releases.json', 'utf8');
const data = JSON.parse(content);

const comp = process.argv[process.argv.length - 1];

for (const asset of data.assets) {
  if (asset.name && asset.name.indexOf(comp) > -1) {
    console.log(asset.browser_download_url);
  }
}

