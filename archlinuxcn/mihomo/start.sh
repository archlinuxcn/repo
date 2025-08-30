#!/usr/bin/bash

confDir=/var/tmp/clash-conf

if [ -d "${confDir}" ]; then
	rm -rf "${confDir}"
fi

mkdir -p "${confDir}"

cp "${CREDENTIALS_DIRECTORY}/config.yaml" "${confDir}"/config.yaml

clash-meta -d /var/tmp/clash-conf