#!/usr/bin/bash

mkdir -p ~/.local/share/PrismLauncher

export _portableConfig="org.prismlauncher.PrismLauncher"

if [[ "$@" = "--actions opendir" ]]; then
	portable --actions opendir
elif [[ "$@" = "--actions share-files" ]]; then
	portable --actions share-files
elif [[ "$@" = "--actions quit" ]]; then
	portable --actions quit
else
	portable -- $@
fi

