#!/bin/sh

## configuration
# proton executable
_proton=echo
# default prefix dir if STEAM_COMPAT_DATA_PATH not set
_pfx=${XDG_DATA_HOME:-~/.local/share}/proton-pfx
# default appid if STEAM_COMPAT_DATA_PATH or SteamAppId not set nor given as an argument
_appid=0
# default mode of execution if not given as an argument
_mode=waitforexitandrun

## functions
set_env(){
# TODO: all the env that proton did not set itself, but steam
#export GST_PLUGIN_SYSTEM_PATH_1_0=/home/gloriouseggroll/.steam/steam/compatibilitytools.d/Proton-5.11-GE-2-MF/dist/lib64/gstreamer-1.0:/home/gloriouseggroll/.steam/steam/compatibilitytools.d/Proton-5.11-GE-2-MF/dist/lib/gstreamer-1.0
#export WINE_GST_REGISTRY_DIR=/home/gloriouseggroll/Games/origin/gstreamer-1.0/
#export WINEUSERNAME=$USER
# No data path to prefix? Let's set the default path. We want to include the AppId in the path like steam.
if [ -z ${STEAM_COMPAT_DATA_PATH+x} ]; then
  export STEAM_COMPAT_DATA_PATH=${_pfx}/${SteamAppId:-${_appid}}
  echo "ProtonLauncher[$$] INFO: empty STEAM_COMPAT_DATA_PATH set to ${STEAM_COMPAT_DATA_PATH}"
elif ! [ ${SteamGameId} -ge 0 ] 2>/dev/null && ! [ ${SteamAppId} -ge 0 ] 2>/dev/null && ! [ $(basename ${STEAM_COMPAT_DATA_PATH}) -ge 0 ] 2>/dev/null; then
  export SteamAppId=${_appid}
  echo "ProtonLauncher[$$] INFO: empty SteamAppId set to ${SteamAppId}"
fi
# If the prefix path does not exist yet, we will create it.
if ! [ -d ${STEAM_COMPAT_DATA_PATH} ]; then
  install -d ${STEAM_COMPAT_DATA_PATH} || exit 1
  echo "ProtonLauncher[$$] INFO: directory ${STEAM_COMPAT_DATA_PATH} created"
fi
# argument -e was provided, so summerize the relevant env we set so far.
if [ ${_printenv} == "true" ] 2>/dev/null; then print_env; fi
}

print_usage(){
cat <<EOF

USAGE:  proton executable.exe
        proton [mode]  executable.exe
        proton [appid] executable.exe
        proton [--environment|-e] [--help|-h]

EOF
}

print_help(){
print_usage
cat <<EOF
ENV:    STEAM_COMPAT_DATA_PATH
        SteamAppId
        SteamGameId

Just call this proton launcher script with your app as the only argument
to run it with the default prefix
$_pfx/$_appid and default mode "$_mode".

_mode_
You can change the mode of operation by specifying it as the first argument.
Possible values are: waitforexitandrun, run, getcompatpath, getnativepath

_appid_
Protonfixes uses three environment variables to determine the application to
run fixes for. The env STEAM_COMPAT_DATA_PATH points to the wine prefix and
usually includes the AppId. If the env SteamAppId (or SteamGameId) is set, it
takes precedence as the AppId used.

As proton itself needs the env STEAM_COMPAT_DATA_PATH, the default prefix
$_pfx/$_appid is used when it is not set or empty.
An AppId given by env SteamAppId will alter this path accordingly.

Provide "appid" as an argument instead of "mode" to change the AppId regardless
of the env vars. In this case, the mode defaults to "$_mode".
Useable for "appid": see https://steamdb.info/apps/

Note that the env SteamGameId is not set by this launcher script in any case.
This env is evaluated by steam executables inside the prefix. Set it yourself
as you see fit.

To see the current ENV when this script is called, use "-e" the switch.

EOF
}

print_env(){
cat <<EOF

Current ENVIRONMENT variables:

STEAM_COMPAT_DATA_PATH  ${STEAM_COMPAT_DATA_PATH:-"Empty or not set."}
SteamAppId              ${SteamAppId:-"Empty or not set."}
SteamGameId             ${SteamGameId:-"Empty or not set."}
EOF
}

## main
if [ "$1" == "--help" ] || [ "$1" == "-h" ]; then print_help; exit 0; fi
if [ "$1" == "--environment" ] || [ "$1" == "-e" ]; then _printenv=true; shift; fi

case $# in
  0)
    print_usage
    ;;
  1)
    # just start an application with default appid and mode
    set_env
    ${_proton} ${_mode} "$1"
    ;;
  *)
    if ! [ "$1" -ge 0 ] 2>/dev/null; then
      # start proton with given arguments, compatible with standard proton invokation
      set_env
      ${_proton} "${@}"
    else
      # first arg is a positive signed int, thus the appid
      export SteamAppId="$1"
      #export SteamGameId="$1"
      echo "ProtonLauncher[$$] INFO: forcing SteamAppId to $1"
      set_env
      ${_proton} ${_mode} "${@:2}"
    fi
    ;;
esac
