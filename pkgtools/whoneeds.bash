#! /bin/bash

echo "Packages that depend on [$1]"
comm -12 <(pactree -ru $1|sort) <(pacman -Qqe|sort) | grep -v ^$1$ | sed 's/^/  /'
