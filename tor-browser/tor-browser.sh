#!/usr/bin/env bash

# Copyright (C) 2009 Benjamin Drung <bdrung at ubuntu dot com>
# Copyright (C) 2012 Alessio Sergi <al3hex at gmail dot com>
# modified 2012 for tor-browser (Max Roder <maxroder at web dot de>)
# modified 2014 by Yardena Cohen <yardenack at gmail dot com>
# modified 2017 by grufo <madmurphy333 at gmail dot com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

set -e


# filled by PKGBUILD
_TB_PKGNAME_='__REPL_NAME__'
_TB_VERSION_='__REPL_VERSION__'
_TB_RELEASE_='__REPL_RELEASE__'
_TB_LANGUAGE_="__REPL_LANGUAGE__"
_TB_ARCH_='__REPL_ARCH__'

# other constants and variables
_TB_HOME_DIR_=~/".${_TB_PKGNAME_}"
_TB_APP_DIR_="${_TB_HOME_DIR_}/app"
_TB_VER_FILE_="${_TB_HOME_DIR_}/VERSION"
_TB_LOG_FILE_="${_TB_HOME_DIR_}/LOG"
_TB_UPDATE_=0


# syntax: _notify_ "${TITLE}" "${MESSAGE}"
_notify_() {

	if [ $(which zenity 2>/dev/null) ]; then
		zenity --info --title "${1}" --text "${2}"
	elif [ $(which notify-send 2>/dev/null) ]; then
		notify-send "${1}" "${2}"
	elif [ $(which kdialog 2>/dev/null) ]; then
		kdialog --title "${1}" --passivepopup "${2}"
	else
		echo -e "${0}: [${1}] ${2}" >&2
	fi

}


# syntax: _compare_ver_ "${INSTALLED_VERSION}" "${LATEST_VERSION}"
_compare_ver_() {

	[[ "${1}" == "${2}" ]] && return 1 || [[ "${1}" == "`echo -e "${1}\n${2}" | sort -V | head -n1`" ]]

}


_refresh_local_() {

	echo "${0}: Extracting files to ${_TB_APP_DIR_}." >> "${_TB_LOG_FILE_}"
	rm -rf "${_TB_APP_DIR_}"/*
	tar --strip-components=1 -xJf "/opt/${_TB_PKGNAME_}/tor-browser-${_TB_ARCH_}-${_TB_VERSION_}_${_TB_LANGUAGE_}.tar.xz" \
		-C "${_TB_APP_DIR_}" >> "${_TB_LOG_FILE_}" 2>&1 || _notify_ 'Error' \
		"The tor-browser archive could not be extracted to your home directory. \
		\nCheck permissions of ${_TB_APP_DIR_}. \
		\nThe error log can be found in ${_TB_LOG_FILE_}."

	[[ -f "${_TB_APP_DIR_}/Browser/start-tor-browser" ]] && echo "${_TB_VERSION_}" > "${_TB_VER_FILE_}"

}


_aur_update_() {

	local DO_UPDATE=0
	local AUR_URL="https://aur.archlinux.org/cgit/aur.git/snapshot/${_TB_PKGNAME_}.tar.gz"

	if [[ "$(id -u)" == '0' ]]; then
		echo 'It is not a good idea to do this as root. Abort.' 1>&2
		exit 1
	fi

	if ! curl --output /dev/null --silent --head --fail "${AUR_URL}"; then
		echo 'Unable to retrieve the PKGBUILD. Abort.'
		exit 1
	fi

	local TMP_PKGBUILD="$(mktemp -d)"

	cd "${TMP_PKGBUILD}"

	curl --silent "${AUR_URL}" | tar xz

	cd "${TMP_PKGBUILD}/${_TB_PKGNAME_}"

	local AUR_VERSION="$(grep 'pkgver' '.SRCINFO' | cut -d = -f2 | sed -e 's/^[[:space:]]*//')"
	local AUR_RELEASE="$(grep 'pkgrel' '.SRCINFO' | cut -d = -f2 | sed -e 's/^[[:space:]]*//')"

	if _compare_ver_ "${_TB_VERSION_}" "${AUR_VERSION}"; then
		echo 'Found new version.'
		local DO_UPDATE=1
	elif [[ "${_TB_VERSION_}" == "${AUR_VERSION}" ]] && [[ "${_TB_RELEASE_}" != "${AUR_RELEASE}" ]] && [[ "${_TB_RELEASE_}" == "`echo -e "${_TB_RELEASE_}\n${AUR_RELEASE}" | sort | head -n1`" ]]; then
		echo 'Found new PKGBUILD.'
		local DO_UPDATE=1
	else
		echo "Everything is up to date (version: ${_TB_VERSION_})"
	fi

	[[ ${DO_UPDATE} -eq 1 ]] && makepkg -si

	rm -rf "${TMP_PKGBUILD}"

}


_usage_() {

	cat <<EOF
Usage: ${0##*/} [option]

Options:
  -h|--help         Show this help message and exit
  -u|--update       Search in AUR for a new release and install it
  -f|--refresh      Force refresh of the copy in your home directory
  --dir=<directory> The Tor-Browser directory to use

  All unrecognized arguments will be passed to the browser.
EOF

}


# remove old INSTALL and APP directories (temporary command, to be removed in the next versions)
if [[ -d "${_TB_HOME_DIR_}/INSTALL" ]] || [[ -d "${_TB_HOME_DIR_}/APP" ]]; then
	rm -rf "${_TB_HOME_DIR_}"
fi

args=()
for arg; do
	case "${arg}" in
		-h|--help) _usage_; exit 0 ;;
		-u|--update) _aur_update_; exit 0 ;;
		-f|--refresh) _TB_UPDATE_=1 ;;
		--dir=*) _TB_HOME_DIR_="${arg#*=}" ;;
		*) args+=("$arg") ;;
	esac
done

# create directory, if it is missing (e.g. first run)
[[ ! -d "${_TB_APP_DIR_}" ]] && mkdir -p "${_TB_APP_DIR_}"
cd "${_TB_HOME_DIR_}"

# create version file if missing
[[ ! -f "${_TB_VER_FILE_}" ]] && echo 0 > "${_TB_VER_FILE_}"

# get the installed version
while read line
do
	TB_INSTALLED_VERSION="${line}"
done < "${_TB_VER_FILE_}"

# start update if old or no tor-browser is installed
if [[ "${TB_INSTALLED_VERSION}" == "${_TB_VERSION_}" ]] && [[ ${_TB_UPDATE_} -eq 0 ]]; then
	# clear log
	> "${_TB_LOG_FILE_}"
else
	echo "${0}: Your version in ${_TB_HOME_DIR_} is outdated or you do not have installed ${_TB_PKGNAME_} yet." > "${_TB_LOG_FILE_}"
	_refresh_local_
fi

# start tor-browser
cd "${_TB_APP_DIR_}/Browser" && ./start-tor-browser "${args[@]}"

