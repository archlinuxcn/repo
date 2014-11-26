#!/bin/bash
#
# aurvote : Tool to vote for favorite AUR packages
#
# Copyright (c) 2007-2010 Julien MISCHKOWITZ <wain@archlinux.fr>
# Copyright (c) 2011 tuxce <tuxce.net@gmail.com>
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU Library General Public License as published
# by the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

NAME='aurvote'
VERSION=1.8

TMPDIR=${TMPDIR:-/tmp}
AV_TMP="$TMPDIR/aurvote-$USER"

CONFIGFILE=${XDG_CONFIG_HOME:-~/.config}/aurvote

AUR_URL="https://aur.archlinux.org"
AUR_URL_LOGIN="$AUR_URL/login/"
AUR_URL_PKG_INFO="$AUR_URL/rpc.php?type=info&arg="
AUR_URL_PKG_PAGE="$AUR_URL/packages/"
AUR_URL_PKG_ACTION="$AUR_URL/pkgbase/"
AUR_DOMAIN="aur.archlinux.org"
AUR_COOKIE="AURSID"
AUR_COOKIE_VALUE=""
AUR_SETLANG="?setlang=en"
AUR_TOKEN=""

version() {
    echo "$NAME $VERSION"
}

usage() {
    echo "$NAME $VERSION"
    echo
    echo "usage: $0 <option> <pkgname1> <pkgname2> ..."
    echo
    echo " --version, -V       shows version"
    echo " --help,    -h       shows this help"
    echo " --check,   -c       check for voted packages"
    echo " --vote,    -v       vote for packages"
    echo " --unvote,  -u       unvote packages"
    echo
    echo " --configure         create $CONFIGFILE"
    echo
}

error() {
    echo -e "Error: $*"
    exit 1
}

is_cookie_valid() {
    [[ -r $COOKIE_FILE ]] || return 1
    local expire
    expire=$(sed -ne '/^\(#HttpOnly_\|[^#]\)/ { s/#HttpOnly_//;p }' "$COOKIE_FILE" |
        awk "{ if (\$1==\"$AUR_DOMAIN\" && \$6==\"$AUR_COOKIE\") print \$5\" \"\$7; }")
    AUR_COOKIE_VALUE=${expire##* }
    expire=${expire%% *}
    [[ $expire ]] && { ((expire==0)) || ((expire>$(date +%s))); }
}

aur_login() {
    local args=()
    if ((PERSIST)); then
        is_cookie_valid && return 0
        args=(-d "remember_me=on")
    fi
    if [[ ! $user || ! $pass ]]; then
        error "$CONFIGFILE must have user name and password. Run:\n$NAME --configure"
    fi
    curl $CURL_OPT -L -fs -c "$COOKIE_FILE" "${args[@]}" -d "user=$user" \
         --data-urlencode "passwd=$pass" "$AUR_URL_LOGIN" \
         -o "$AV_TMP/login" || error "Unable to access $AUR_URL_LOGIN"
    err=$(sed -ne 's/.*ul class="errorlist"><li>\([^<]*\)<.*/\1/p' "$AV_TMP/login")
    [[ $err ]] && error "$err"
}

aur_get_pkg_page() {
    local pkg=$1
    curl $CURL_OPT -fs -b "$COOKIE_FILE" \
        "${AUR_URL_PKG_PAGE}${pkg}${AUR_SETLANG}" \
        -o "$AV_TMP/$pkg.$PID" ||
        error "Unable to get $pkg page"
}

aur_set_token() {
    aur_get_pkg_page "$1"
    AUR_TOKEN=$(sed -n -e '/<input type="hidden" name="token"/ { s/.*value="\([0-9a-f]\+\)".*/\1/p;q }' "$AV_TMP/$pkg.$PID")
    [[ ! $AUR_TOKEN ]] && error "Unable to get token from AUR page"
}

aur_check_vote() {
    local pkg
    for pkg in "${pkgnames[@]}"; do
        aur_get_pkg_page "$pkg"
        if sed '/<div id="news">/q' "$AV_TMP/$pkg.$PID" | grep -q /unvote/; then
            echo "already voted"
        elif sed '/<div id="news">/q' "$AV_TMP/$pkg.$PID" | grep -q /vote/; then
            echo "not voted"
        else
            echo "voted status not found"
        fi
    done
}


aur_vote() {
    local pkg vote action ret pkgbase
    if (($1)); then
        vote="/vote/"
        action=do_Vote
    else
        vote="/unvote/"
        action=do_UnVote
    fi
    for pkg in "${pkgnames[@]}"; do
        [[ ! $AUR_TOKEN ]] && aur_set_token "$pkg"
        curl $CURL_OPT -fs -b "$COOKIE_FILE" \
             "${AUR_URL_PKG_ACTION}${pkg}${vote}" \
             -d token="$AUR_TOKEN" \
             -d "$action"="(Un)Vote" \
             -o /dev/null
        ret=$?
        if ((ret == 22)); then
            pkgbase=$(curl $CURL_OPT -fs "${AUR_URL_PKG_INFO}${pkg}" | sed -e 's|.*"PackageBase": *"\([^"]*\)".*|\1|')
            [[ $pkgbase ]] && curl $CURL_OPT -fs -b "$COOKIE_FILE" \
                 "${AUR_URL_PKG_ACTION}${pkgbase}${vote}" \
                 -d token="$AUR_TOKEN" \
                 -d "$action"="(Un)Vote" \
                 -o /dev/null
            ret=$?
        fi
        if ((ret)); then
            echo "Error: Can't (un)vote for $pkg"
        else
            echo "$pkg : vote changed"
        fi
    done
}

create_config_file() {
    local ans configdir=${CONFIGFILE%/*}
	if [[ ! -d $configdir ]]; then
		mkdir -p "$configdir" || error "Unable to create $configdir"
	fi
    if [[ -f "$CONFIGFILE" ]]; then
        read -p "$CONFIGFILE exists. Replace ? [y/N] " ans
        [[ $ans != 'Y' && $ans != 'y' ]] && return 0
    fi
    echo -n > "$CONFIGFILE"
    if [[ ! -r "$CONFIGFILE" ]]; then
        error "Unable to create $CONFIGFILE"
    fi
    echo "Creation of $CONFIGFILE"
    read -p "AUR User : " ans
    printf "user=%q\n" "$ans" >> "$CONFIGFILE"
    read -p "AUR Password : " ans
    printf "pass=%q\n" "$ans" >> "$CONFIGFILE"
    read -p "Persistent login ? [Y/n] " ans
    [[ $ans = 'n' || $ans = 'N' ]] && return 0
    read -p "Path to the cookie file : [/var/tmp/aurvote-$USER.cookie] ? " ans
    printf "COOKIE_FILE=%q\n" "${ans:-/var/tmp/aurvote-$USER.cookie}" >> "$CONFIGFILE"
    echo
    echo "Creation complete."
}

### MAIN PROGRAM ###
umask 077
[[ -d "$AV_TMP" ]] || mkdir -p "$AV_TMP"
[[ -d "$AV_TMP" && -w "$AV_TMP" ]] || error "Cannot access to $AV_TMP"
PID=$$
ACTION="vote"
pkgnames=()
CURL_OPT=""
PERSIST=0

[[ -r "$CONFIGFILE" ]] && source "$CONFIGFILE"

[[ $COOKIE_FILE ]] && PERSIST=1

while [[ $1 ]]; do
    case $1 in
        --help|-h)    usage; exit 0;;
        --version|-V) version; exit 0;;
        --check|-c)   ACTION="check";;
        --configure)  ACTION="configure";;
        --vote|-v)    ACTION="vote";;
        --unvote|-u)  ACTION="unvote";;
        --id)         ;; # deprecated
        --insecure)   CURL_OPT+=" --insecure";; 
        -k)           PERSIST=1; shift; COOKIE_FILE="$1";;
        --*|-*)       usage; exit 1;;
        *)            pkgnames+=("$1");;
    esac
    shift
done

if [[ $ACTION = "configure" ]]; then
    create_config_file
    exit 0
fi

COOKIE_FILE=${COOKIE_FILE:-"$AV_TMP/cookies"}
pkgnames=("${pkgnames[@]%/*}") # compatibility with yaourt <= 1.2.1
[[ ! $pkgnames ]] && usage && exit 1
 
aur_login

case "$ACTION" in
    check)  aur_check_vote;;
    vote)   aur_vote 1;;
    unvote) aur_vote 0;;
esac

# vim: set ts=4 sw=4 et:
