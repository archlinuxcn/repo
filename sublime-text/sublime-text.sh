#!/bin/bash

# Please note that Sublime Text 2 for some reason opens an empty instance
# if the project you're trying to open is already open in another instance,
# instead of just giving it focus.

BIN=/opt/sublime-text/sublime_text

PID=$(ps -Ao comm,pid | awk '$1 == "sublime_text" { print $2 }')
ARGS="--class=sublime_text"

if [[ ${1:(-16)} == ".sublime-project" ]]; then
	ARGS="${ARGS} --project"
fi

# LD_LIBRARY_PATH is needed for old libpng

if [[ -n ${PID} ]]; then
	LD_LIBRARY_PATH=/opt/sublime-text/lib ${BIN} ${ARGS} "$@"
else
	LD_LIBRARY_PATH=/opt/sublime-text/lib ${BIN} ${ARGS} "$@" &
fi
