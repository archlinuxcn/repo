'use strict';

const PATCHABLE_FILE = './package.json';

const fs = require('fs');
const data = JSON.parse(fs.readFileSync(PATCHABLE_FILE));

// remove extra dependencies
const removePkg = [
	/^chai$/,
	/^electron-/,
	/^electron$/,
	/^eslint-/,
	/^eslint$/,
	/^grunt-contrib-compress$/,
	/^grunt-contrib-deb$/,
	/^grunt-contrib-watch$/,
	/^grunt-electron$/,
	/^grunt-eslint$/,
	/^mocha$/,
	/^puppeteer$/,
	/^stats-webpack-plugin$/,
	/^sumchecker$/,
	/^webpack-bundle-analyzer$/,
	/^webpack-dev-server$/,
	/keeweb-native-messaging-host$/,
	/keeweb-native-modules$/,
];

Object.keys(data.dependencies).forEach(dep => {
	if (removePkg.some(re => re.test(dep)))
		delete data.dependencies[dep];
});

fs.writeFileSync(PATCHABLE_FILE, JSON.stringify(data, null, '\t'));
