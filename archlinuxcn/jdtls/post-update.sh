#!/bin/bash

set -exuo pipefail

uid="$(id -u)"

# Move pkgrel back to 1 after a version bump
sed -i 's/pkgrel=.*/pkgrel=1/' ./PKGBUILD

# Update download URLs and checksums
new_version="$(grep 'pkgver=' PKGBUILD | cut -d = -f 2)"
filename="$(curl --fail "https://download.eclipse.org/jdtls/milestones/${new_version}/latest.txt" | head -n 1)"
sha256="$(curl --fail "https://download.eclipse.org/jdtls/milestones/${new_version}/${filename}.sha256")"

sed -i "s%source=(\".*\"%source=(\"https://download.eclipse.org/jdtls/milestones/${new_version}/${filename}\"%" ./PKGBUILD
sed -i "s%sha256sums=('.*'%sha256sums=('${sha256}'%" ./PKGBUILD

# Update the .SRCINFO file to match the new version. The easiest and most
# consistent way to do this is by using the archlinux-provided tools for this.
# Because renovate doesn't run in an arch container, use docker to spin up a
# temporary container for this purpose.  makepkg in this container cannot be
# run as root. Therefore, create a temporary user for this. This used need to
# use the UID of the host's user to avoid file access problems when using bind
# mounts in docker.
docker run --rm -v "$(pwd):/pkg" archlinux:latest bash -c "
set -exuo pipefail
pacman -Syu --noconfirm binutils
useradd -u ${uid} builder
cd /pkg
su builder -c 'makepkg --printsrcinfo > .SRCINFO'
"
