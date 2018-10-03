#!/usr/bin/electron

var APP_DIR = '/usr/share/typora/';
var conf = require(APP_DIR + 'package.json')

process.argv.shift();
require(APP_DIR + conf.main);
