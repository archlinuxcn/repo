#!/usr/bin/electron

const name = 'code-oss';

const app = require('electron').app;
const path = require('path');
const fs = require("fs");

// Change command name.
const fd = fs.openSync("/proc/self/comm", fs.constants.O_WRONLY);
fs.writeSync(fd, name);
fs.closeSync(fd);

// Remove first command line argument (/usr/lib/code/code.js). - We call the CLI file first
process.argv.splice(0, 1);

// Set application paths.
const appPath = __dirname;
const packageJson = require(path.join(appPath, 'package.json'));
app.setAppPath(appPath);
app.setDesktopName(name + '.desktop');
app.setName(name);
app.setPath('userCache', path.join(app.getPath('cache'), name));
app.setPath('userData', path.join(app.getPath('appData'), name));
app.setVersion(packageJson.version);

// Run the application.
require('module')._load(appPath, module, true);

