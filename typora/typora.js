#!/usr/bin/electron

const { join } = require('path');
const { app } = require('electron');

const APP_DIR = '/usr/share/typora/';

const conf = require(APP_DIR + 'package.json');

app.setName(conf.name);
app.setPath('userData', join(app.getPath('appData'), conf.name));
app.getVersion = () => conf.version;

process.argv.shift();
require(APP_DIR + conf.main);
