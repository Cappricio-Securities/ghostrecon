#!/usr/bin/env node
/**
 * gh0str3con
 * gh0str3con is a All in one cloud based web Recon tool.
 *
 * @author karthikeyan V (karthithehacker) <https://karthithehacker.com>
 */
const CONST = require('./includes/const');
const express = require("express");
const app = express();
const help = require('./includes/help');
const bodyParser = require('body-parser');
const os = require("os");
const yargs = require('yargs/yargs');
const { hideBin } = require('yargs/helpers')
// get the home directory path

help.helpintro();
console.log("URL=====> http://localhost:"+8090)

app.listen(8090);
app.set('view-engine','ejs');
app.use(bodyParser.json({limit: "50mb"}));
app.use(bodyParser.urlencoded({limit: "50mb", extended: true, parameterLimit:50000}));
app.use(express.static(__dirname + '/Assets/'));
app.use(require('./includes/route'));
