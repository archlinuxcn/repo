#!/bin/sh

sed -i -e 's/\([[:blank:]]*\)lint_[_a-zA-Z0-9]*\(.*\)/\1true\2/' /usr/bin/makepkg
