#!/usr/bin/bash

confDir="${STATE_DIRECTORY}"/conf

mkdir -p "${confDir}"

install "${CREDENTIALS_DIRECTORY}/config.yaml" "${confDir}"/config.yaml
install /etc/clash/Country.mmdb -t "${confDir}"