#!/usr/bin/env bash

#
# This script is used to test AUR builds locally in a clean Arch Linux Docker container.
# It is not used in the AUR builds in any way, and is only for debugging purposes.
#

set -e

docker run --rm -v $(pwd):/tmp/output -v $(pwd)/dockerscript.sh:/root/dockerscript.sh archlinux:base-devel /bin/bash /root/dockerscript.sh
