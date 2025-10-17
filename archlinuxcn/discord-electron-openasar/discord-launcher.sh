#!/usr/bin/env bash

set -euo pipefail

declare -a flags
declare -l PATCH_KRISP

[[ -r "${XDG_CONFIG_HOME:-$HOME/.config}/@PKGNAME@.conf" ]] && source "${XDG_CONFIG_HOME:-$HOME/.config}/@PKGNAME@.conf"

flags_file="${XDG_CONFIG_HOME:-$HOME/.config}/@PKGNAME@-flags.conf"
krisp_bin="${DISCORD_USER_DATA_DIR:-${XDG_CONFIG_HOME:-$HOME/.config}/@PKGNAME@}/@PKGVER@/modules/@PKGNAME@_krisp/@PKGNAME@_krisp.node"

if [[ "${PATCH_KRISP:-}" == true ]] && [[ -w "${krisp_bin}" ]]; then
	if hash python &> /dev/null && python -c 'import capstone; import elftools' &> /dev/null; then
		# Patch Krisp binary to ignore signature check
		echo -n 'Running Krisp patcher... '
		python /usr/lib/@PKGNAME@/krisp-patcher.py "${krisp_bin}"
	fi
fi

if [[ -r "${flags_file}" ]]; then
	# Replacing because old flag does not work
	if [[ -w "${flags_file}" ]] && grep -q '\--ignore-gpu-blacklist' "${flags_file}"; then
		sed -i 's|--ignore-gpu-blacklist|--ignore-gpu-blocklist|' "${flags_file}"
	fi
	mapfile -t < "${flags_file}"
fi

for line in "${MAPFILE[@]}"; do
	if [[ ! "${line}" =~ ^[[:space:]]*#.* ]] && [[ -n "${line}" ]]; then
		flags+=("${line}")
	fi
done

if [[ -e "${XDG_RUNTIME_DIR:-}/${WAYLAND_SOCKET:-}" || -e "${WAYLAND_DISPLAY:-}" || "${XDG_SESSION_TYPE:-}" == "wayland" ]]; then
	# work around electron's broken wayland detection
	# TODO: remove when Arch updates to an electron release that includes the fix
	# https://github.com/electron/electron/pull/48301
	flags+=("--ozone-platform=wayland")
fi

unset flags_file krisp_bin


exec /usr/lib/@ELECTRON@/electron \
	/usr/lib/@PKGNAME@/resources/app.asar \
	"${flags[@]}" "$@"
