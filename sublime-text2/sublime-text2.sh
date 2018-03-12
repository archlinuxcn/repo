#!/bin/bash

ST=/opt/sublime-text2

# needed for .desktop launcher
ARGS="--class=sublime_text"

# Note: Sublime Text 2 opens an empty instance if the project to open is
# already opened in another instance instead of just giving it focus.
if [[ ${1:(-16)} == ".sublime-project" ]]; then
  ARGS="${ARGS} --project"
fi

# LD_LIBRARY_PATH is needed for old libpng
export LD_LIBRARY_PATH=${ST}/lib:${LD_LIBRARY_PATH}

exec ${ST}/sublime_text ${ARGS} "$@" &
