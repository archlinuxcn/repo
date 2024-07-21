#!/bin/bash

## configuration
# proton executable
_proton=echo
# default prefix dir if STEAM_COMPAT_DATA_PATH not set
_pfx=${XDG_DATA_HOME:-~/.local/share}/proton-pfx
# default dxvk state cache path if not set, could be compatible with dxvk-cache-pool application
_cachepath=${XDG_CACHE_HOME:-~/.cache}/dxvk-cache-pool
# default appid if STEAM_COMPAT_DATA_PATH or SteamAppId not set nor given as an argument
_appid=0
# default mode of execution if not given as an argument
_mode=waitforexitandrun
# default steam install path (don't worry, you still don't need steam)
_steam=${XDG_DATA_HOME:-~/.local/share}/Steam

## functions
set_env() {
	# Proton now cares about steam install - it wants to update the tracked files according to installed steam.
	# While this makes no sense in standalone, we need to set *some* path even if does not exists.
	if [ -z ${STEAM_COMPAT_CLIENT_INSTALL_PATH+x} ]; then
		export STEAM_COMPAT_CLIENT_INSTALL_PATH=${_steam}
		>&2 echo "ProtonLauncher[$$] INFO: empty STEAM_COMPAT_CLIENT_INSTALL_PATH set to ${STEAM_COMPAT_CLIENT_INSTALL_PATH}"
	fi
	if ! [ -d "${STEAM_COMPAT_CLIENT_INSTALL_PATH}" ]; then
		>&2 echo "ProtonLauncher[$$] WARN: directory ${STEAM_COMPAT_CLIENT_INSTALL_PATH} does not exist"
	fi

	# No data path to prefix? Let's set the default path. We want to include the AppId in the path like steam.
	if [ -z ${STEAM_COMPAT_DATA_PATH+x} ]; then
		export STEAM_COMPAT_DATA_PATH=${_pfx}/${SteamAppId:-${_appid}}
		>&2 echo "ProtonLauncher[$$] INFO: empty STEAM_COMPAT_DATA_PATH set to ${STEAM_COMPAT_DATA_PATH}"
	elif ! [ "${SteamGameId}" -ge 0 ] 2>/dev/null && ! [ "${SteamAppId}" -ge 0 ] 2>/dev/null && ! [ "$(basename "${STEAM_COMPAT_DATA_PATH}")" -ge 0 ] 2>/dev/null; then
		export SteamAppId=${_appid}
		>&2 echo "ProtonLauncher[$$] INFO: empty SteamAppId set to ${SteamAppId}"
	fi
	# If the prefix path does not exist yet, we will create it.
	if ! [ -d "${STEAM_COMPAT_DATA_PATH}" ]; then
		install -d "${STEAM_COMPAT_DATA_PATH}" || exit 1
		>&2 echo "ProtonLauncher[$$] INFO: directory ${STEAM_COMPAT_DATA_PATH} created"
	fi

	# DXVK state cache path not given, we will use a default.
	if [ -z ${DXVK_STATE_CACHE_PATH+x} ]; then
		export DXVK_STATE_CACHE_PATH=${_cachepath}
		>&2 echo "ProtonLauncher[$$] INFO: empty DXVK_STATE_CACHE_PATH set to ${_cachepath}"
	fi
	# If the state cache path does not exist yet, we will create it.
	if ! [ -d "${DXVK_STATE_CACHE_PATH}" ]; then
		install -d "${DXVK_STATE_CACHE_PATH}" || exit 1
		>&2 echo "ProtonLauncher[$$] INFO: directory ${DXVK_STATE_CACHE_PATH} created"
	fi

	# Placeholder in case we need the workaround again when tracked_files missing
	if ! [ -f "${STEAM_COMPAT_DATA_PATH}"/tracked_files ]; then
		if [ -f "${STEAM_COMPAT_DATA_PATH}"/version ]; then
			>&2 echo "ProtonLauncher[$$] WARN: file ${STEAM_COMPAT_DATA_PATH}/tracked_files missing! Please report to AUR maintainer"
		fi
	fi

	# argument -e was provided, so summarize the relevant env we set so far.
	if [ "${_printenv}" == "true" ] 2>/dev/null; then print_env; fi
}

print_usage() {
	cat <<EOF

USAGE:  proton [--environment|-e] executable.exe
        proton [--environment|-e] [mode]  executable.exe
        proton [--environment|-e] [appid] executable.exe
        proton [--help|-h]

EOF
}

print_help() {
	print_usage
	cat <<EOF
ENV:    STEAM_COMPAT_DATA_PATH
        STEAM_COMPAT_CLIENT_INSTALL_PATH
        DXVK_STATE_CACHE_PATH
        SteamAppId
        SteamGameId

Just call this proton launcher script with your app as the only argument
to run it with the default prefix
${_pfx}/${_appid} and default mode "${_mode}".

Use other invocations as stated with USAGE: and/or modify behavior with
environment variables as described below.

_mode_

You can change the mode of operation by specifying it as the first argument.
Possible values are: waitforexitandrun, run, getcompatpath, getnativepath

_appid_

Protonfixes (included by proton-ge) uses three environment variables to
determine the application to run fixes for.
The env STEAM_COMPAT_DATA_PATH points to the wine prefix and usually includes
the AppId, which is used in that case. If the env SteamAppId (or SteamGameId)
is set, it takes precedence as the AppId used by protonfixes.

As proton itself needs the env STEAM_COMPAT_DATA_PATH set, the default prefix
${_pfx}/${_appid} is used when it is not set or empty.
In that case, an AppId given by env SteamAppId or as the first argument will
alter this path accordingly.
If STEAM_COMPAT_DATA_PATH is set, it will not be modified by a provided AppId.

Provide "appid" as the first argument to change the AppId regardless of
the env vars (force). In this case, the mode defaults to "${_mode}".
Useable for "appid": see https://steamdb.info/apps/

_other_

The env STEAM_COMPAT_CLIENT_INSTALL_PATH is set to "${_steam}" if not given,
because proton cares. It has no effect if proton is not started from
within steam anyway, therefore the path does not have to be actually resolvable.

DXVK creates cache files right next to the executable if the env
DXVK_STATE_CACHE_PATH is missing.
This launcher sets it to "${_cachepath}"
if not provided. It makes sharing of those files as well as read-only game
folders possible. Also, the cache survives remove/reinstall of the game.

You may share oder download caches for example from here:
https://github.com/begin-theadventure/dxvk-caches/

Note that the env SteamGameId is not set by this launcher script in any case.
This env is evaluated by steam executables inside the prefix. Set it yourself
if you see fit.

To print the current env when this script is called, use the "-e" switch.

_example invocations_

# "${_mode}" winecfg in prefix ${_pfx}/${_appid}
$ proton winecfg

# "${_mode}" winecfg in prefix ${_pfx}/${_appid}, dump all env that have been set
$ proton -e winecfg

# "${_mode}" winecfg in prefix ${_pfx}/17330, matching protonfixes for crysis are run
$ proton 17300 winecfg

# returns native path in ${_pfx}/${_appid}
$ proton getnativepath "C:\Windows"

# "${_mode}" winecfg in prefix ~/myfolder/17300, matching protonfixes for crysis are run
$ env STEAM_COMPAT_DATA_PATH=~/myfolder/17300 proton winecfg

EOF
}

print_env() {
cat <<EOF

Current ENVIRONMENT variables:

STEAM_COMPAT_CLIENT_INSTALL_PATH  ${STEAM_COMPAT_CLIENT_INSTALL_PATH:-"Empty or not set."}
STEAM_COMPAT_DATA_PATH            ${STEAM_COMPAT_DATA_PATH:-"Empty or not set."}
DXVK_STATE_CACHE_PATH             ${DXVK_STATE_CACHE_PATH:-"Empty or not set."}
SteamAppId                        ${SteamAppId:-"Empty or not set."}
SteamGameId                       ${SteamGameId:-"Empty or not set."}
EOF
}

## main
if [ "$1" == "--help" ] || [ "$1" == "-h" ]; then
	print_help
	exit 0
fi
if [ "$1" == "--environment" ] || [ "$1" == "-e" ]; then
	_printenv=true
	shift
fi

case $# in
0)
	print_usage
	;;
1)
	# just start an application with default appid and mode
	set_env
	"${_proton}" "${_mode}" "$1"
	;;
*)
	if ! [ "$1" -ge 0 ] 2>/dev/null; then
		# start proton with given arguments, compatible with standard proton invocation
		set_env
		"${_proton}" "${@}"
	else
		# first arg is a positive signed int, thus the appid
		export SteamAppId="$1"
		#export SteamGameId="$1"
		>&2 echo "ProtonLauncher[$$] INFO: forcing SteamAppId to $1"
		set_env
		"${_proton}" "${_mode}" "${@:2}"
	fi
	;;
esac
