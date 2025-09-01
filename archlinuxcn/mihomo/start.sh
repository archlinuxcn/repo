#!/usr/bin/bash

confDir=/var/lib/private/mihomo/conf

mkdir -p "${confDir}"

install "${CREDENTIALS_DIRECTORY}/config.yaml" "${confDir}"/config.yaml
install /etc/clash/Country.mmdb -t "${confDir}"

clash-meta -d "${confDir}"