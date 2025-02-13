const express = require('express');
const fs = require('fs');
const http = require('http');
const Websocket = require('ws');


/* ----------- CONFIG SETUP ------------- */

const PORT = process.env.PORT || 5000;

const CONFIG = JSON.parse(fs.readFileSync('../config.json'));

