#!/usr/bin/electron

const name = "atom";

const {app} = require("electron");
const fs = require("fs");
const Module = require("module");
const {join} = require("path");
const vm = require("vm");

// Change command name.
const fd = fs.openSync("/proc/self/comm", fs.constants.O_WRONLY);
fs.writeSync(fd, name);
fs.closeSync(fd);

// Remove first command line argument (/usr/bin/electron).
process.argv.splice(0, 1);

// Set application paths.
const appPath = __dirname;
const packageJson = require(join(appPath, "package.json"));
const productName = packageJson.productName;
app.setAppPath(appPath);
app.setDesktopName(name + ".desktop");
app.setName(productName);
app.setPath("userCache", join(app.getPath("cache"), productName));
app.setPath("userData", join(app.getPath("appData"), productName));
app.setVersion(packageJson.version);

// Run the application.
const startupJs = fs.readFileSync(join(appPath, "startup.js"), "utf-8");
vm.runInThisContext(startupJs);
Module._load(appPath, Module, true);
