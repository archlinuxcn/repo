#!/bin/bash

# This script is used to preview and save patch files.

# Current working directory should contain two subdirectories:
# * "org" — with oryginal GTK3 code,
# * "mod" — with modified GTK3 code.
# Patch file is saved under name specified by first argument.

if [[ -d ./org/gtk ]] && [[ -d ./mod/gtk ]] && [[ $1 ]]; then
	command="diff --color -U 5 -r -Z -B ./org ./mod"
	$command > "$1.patch"; reset; $command
fi
