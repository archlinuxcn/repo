#!/usr/bin/bash

install "${CREDENTIALS_DIRECTORY}/config.yaml" "${STATE_DIRECTORY}"/config.yaml
install /etc/clash/Country.mmdb -t "${STATE_DIRECTORY}"
