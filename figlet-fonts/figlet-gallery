#!/bin/sh
ls /usr/share/figlet/fonts/*.flf | cut -d . -f 1 | while read i; do echo "$i.flf:"; figlet -t -f "$i" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890; done | less
