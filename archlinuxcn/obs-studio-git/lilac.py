#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['benklett'])
    add_makedepends(['asio', 'nlohmann-json', 'websocketpp', 'onevpl', 'libdatachannel'])
