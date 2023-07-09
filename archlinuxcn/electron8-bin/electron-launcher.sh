#!/usr/bin/bash

set -euo pipefail

flags_file="${XDG_CONFIG_HOME:-$HOME/.config}/%%PKGNAME%%-flags.conf"

declare -a flags

if [[ -f "${flags_file}" ]]; then
	mapfile -t < "${flags_file}"
fi

for line in "${MAPFILE[@]}"; do
	if [[ ! "${line}" =~ ^[[:space:]]*#.* ]] && [[ -n "${line}" ]]; then
		flags+=("${line}")
	fi
done

exec /usr/lib/%%PKGNAME%%/%%PROJECTNAME%% "${flags[@]}" "$@"
