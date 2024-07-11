#!/usr/bin/env bash

XDG_CONFIG_HOME="${XDG_CONFIG_HOME:-"${HOME}/.config"}"

CONF_FILE="${XDG_CONFIG_HOME}/brave-flags.conf"

if
	test -f "${CONF_FILE}"
then
	mapfile -t CONF_LIST < "${CONF_FILE}"
fi

for CONF_LINE in "${CONF_LIST[@]}"
do
	if ! [[
		"${CONF_LINE}" =~ ^[[:space:]]*(#|$)
	]]
	then
		FLAG_LIST+=("${CONF_LINE}")
	fi
done

export CHROME_VERSION_EXTRA='stable'

exec /opt/brave-bin/brave "${FLAG_LIST[@]}" "${@}"
