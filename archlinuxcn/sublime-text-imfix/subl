#!/bin/sh

# Please note that Sublime Text 2 for some reason opens an empty instance
# if the project you're trying to open is already open in another instance,
# instead of just giving it focus.

SUBLIME_HOME=/opt/sublime-text
LD_LIB=$SUBLIME_HOME/libsublime-imfix.so
BIN=$SUBLIME_HOME/sublime_text

PID=$(ps -Ao comm,pid | awk '$1 == "sublime_text" { print $2 }')
ARGS="--class=sublime-text"

if [[ ${1:(-16)} == ".sublime-project" ]]; then
	ARGS="${ARGS} --project"
fi

if [[ -n ${PID} ]]; then
	LD_PRELOAD=$LD_LIB ${BIN} ${ARGS} "$@"
else
	LD_PRELOAD=$LD_LIB ${BIN} ${ARGS} "$@" &
fi
