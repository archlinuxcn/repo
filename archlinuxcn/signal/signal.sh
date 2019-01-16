#!/bin/sh 
export NODE_ENV=production
electron /usr/lib/signal/resources/app.asar $@
