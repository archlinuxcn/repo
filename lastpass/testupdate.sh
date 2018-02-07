#!/bin/bash

source /usr/share/makepkg/util/message.sh
colorize

if [[ $1 = beta ]]; then
    checkbeta=beta
fi


download_url="$(curl -s https://addons.mozilla.org/en-us/firefox/addon/lastpass-password-manager/versions/"$checkbeta"|grep 'downloads/file'|tac|tee /dev/stderr|tail -1)"
file="$(echo "$download_url"|sed -r 's@.*file/([0-9]+)/.*@\1@g')"
version="$(echo "$download_url"|sed -r 's@.*lastpass_password_manager-([0-9a-z.]+)-.*@\1@g')"

msg2 "pkgver=$version"
msg2 "_file=$file"

if echo "$download_url"|grep -qs data-realurl; then
    error "Not yet reviewed"
fi
