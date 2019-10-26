#!/usr/bin/env bash

# Copyright (C) 2009 Benjamin Drung <bdrung at ubuntu dot com>
# Copyright (C) 2012 Alessio Sergi <al3hex at gmail dot com>
# Copyright (C) 2017 grufo <madmurphy333 at gmail dot com> (Arch User Repository version)
# modified 2012 for tor-browser (Max Roder <maxroder at web dot de>)
# modified 2014 by Yardena Cohen <yardenack at gmail dot com>
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


# CONSTANTS AND VARIABLES

# filled by PKGBUILD
_TB_PKGNAME_='__REPL_NAME__'
_TB_VERSION_='__REPL_VERSION__'
_TB_RELEASE_='__REPL_RELEASE__'
_TB_LANGUAGE_="__REPL_LANGUAGE__"
_TB_ARCH_='__REPL_ARCH__'

# other constants and variables
_TB_HOME_DIR_=~/".${_TB_PKGNAME_}"
_TB_REFRESH_=0


# FUNCTIONS

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

	local KEEP_DIR="${_TB_APP_DIR_}/Browser/TorBrowser/Data/Browser"
	local KEPT_DIR=~/".${_TB_PKGNAME_}-tmpdata"
	local DIR_IS_KEPT=0

	if [[ -d "${KEEP_DIR}" ]]; then
		[[ -d "${KEPT_DIR}" ]] && rm -rf "${KEPT_DIR}"
		mv "${KEEP_DIR}" "${KEPT_DIR}"
		echo "${0}: Preserving files in ${KEPT_DIR}/." >> "${_TB_LOG_FILE_}"
		DIR_IS_KEPT=1
	fi

	echo "${0}: Extracting files to ${_TB_APP_DIR_}." >> "${_TB_LOG_FILE_}"
	rm -rf "${_TB_APP_DIR_}"/*
	tar --strip-components=1 -xJf "/opt/${_TB_PKGNAME_}/tor-browser-${_TB_ARCH_}-${_TB_VERSION_}_${_TB_LANGUAGE_}.tar.xz" \
		-C "${_TB_APP_DIR_}" >> "${_TB_LOG_FILE_}" 2>&1 || _notify_ 'Error' \
		"The tor-browser archive could not be extracted to your home directory. \
		\nCheck permissions of ${_TB_APP_DIR_}. \
		\nThe error log can be found in ${_TB_LOG_FILE_}."

	if [[ ! ${DIR_IS_KEPT} -eq 0 ]]; then
		rm -rf "${KEEP_DIR}"
		mv "${KEPT_DIR}" "${KEEP_DIR}"
	fi

	[[ -f "${_TB_APP_DIR_}/Browser/start-tor-browser" ]] && echo "${_TB_VERSION_}" > "${_TB_VER_FILE_}"

}


_aur_update_() {

	if [[ "$(id -u)" == '0' ]]; then
		echo 'It is not a good idea to do this as root. Abort.' 1>&2
		exit 1
	fi

	local DO_UPDATE=0
	local TMP_PKGBUILD="$(mktemp -d)"

	cd "${TMP_PKGBUILD}"

	if ! { curl --silent --fail "https://aur.archlinux.org/cgit/aur.git/snapshot/${_TB_PKGNAME_}.tar.gz" | tar xz ;} 2>/dev/null; then
		echo 'Unable to retrieve the PKGBUILD. Abort.' 1>&2
		rm -rf "${TMP_PKGBUILD}"
		exit 1
	fi

	cd "${TMP_PKGBUILD}/${_TB_PKGNAME_}"

	local AUR_VERSION="$(grep 'pkgver' '.SRCINFO' | cut -d = -f2 | sed -e 's/^[[:space:]]*//')"
	local AUR_RELEASE="$(grep 'pkgrel' '.SRCINFO' | cut -d = -f2 | sed -e 's/^[[:space:]]*//')"

	if _compare_ver_ "${_TB_VERSION_}" "${AUR_VERSION}"; then
		echo "Found new version (${_TB_VERSION_} -> ${AUR_VERSION})..."
		DO_UPDATE=1
	elif [[ "${_TB_VERSION_}" == "${AUR_VERSION}" ]] && [[ "${_TB_RELEASE_}" != "${AUR_RELEASE}" ]] && [[ "${_TB_RELEASE_}" == "`echo -e "${_TB_RELEASE_}\n${AUR_RELEASE}" | sort | head -n1`" ]]; then
		echo 'Found new PKGBUILD...'
		DO_UPDATE=1
	else
		echo "Everything is up to date (current version: ${_TB_VERSION_})."
	fi

	[[ ! ${DO_UPDATE} -eq 0 ]] && makepkg -si

	rm -rf "${TMP_PKGBUILD}"

}


_usage_() {

	cat <<EOF
Usage: ${0##*/} [option]

Options:
  -h|--help         Show this help message and exit
  -u|--update       Search in AUR for a new release and install it
  -r|--refresh      Refresh the copy in your home directory and launch tor-browser
  -e|--erase        Erase the copy in your home directory
  --dir=<directory> The Tor-Browser directory to use

  All unrecognized arguments will be passed to the browser.
EOF

}


# SCRIPT BODY

args=()
for arg; do
	case "${arg}" in
		-h|--help) _usage_; exit 0 ;;
		-u|--update) _aur_update_; exit 0 ;;
		-f|--refresh) _TB_REFRESH_=1 ;;
		-e|--erase) rm -rf "${_TB_HOME_DIR_}"; exit 0 ;;
		--dir=*) _TB_HOME_DIR_="${arg#*=}" ;;
		*) args+=("$arg") ;;
	esac
done

_TB_VER_FILE_="${_TB_HOME_DIR_}/VERSION"
_TB_LOG_FILE_="${_TB_HOME_DIR_}/LOG"
_TB_APP_DIR_="${_TB_HOME_DIR_}/app"

# create directory, if it is missing (e.g. first run)
[[ ! -d "${_TB_APP_DIR_}" ]] && mkdir -p "${_TB_APP_DIR_}"
cd "${_TB_HOME_DIR_}"

# create version file if missing
[[ ! -f "${_TB_VER_FILE_}" ]] && echo 0 > "${_TB_VER_FILE_}"

# get the installed version
while read _TB_VER_LINE_
do
	_TB_INSTALLED_VERSION_="${_TB_VER_LINE_}"
done < "${_TB_VER_FILE_}"

# start update if old or no tor-browser is installed
if [[ "${_TB_INSTALLED_VERSION_}" == "${_TB_VERSION_}" ]] && [[ ${_TB_REFRESH_} -eq 0 ]]; then
	# clear log
	> "${_TB_LOG_FILE_}"
else
	echo "${0}: Your version in ${_TB_HOME_DIR_} is outdated or you do not have installed ${_TB_PKGNAME_} yet." > "${_TB_LOG_FILE_}"
	_refresh_local_
fi

# start tor-browser
"${_TB_APP_DIR_}/Browser/start-tor-browser" "${args[@]}"

