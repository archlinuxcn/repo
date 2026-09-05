#!/bin/bash

set -euo pipefail

CI_MODE=false
if [[ "$*" == *"--ci"* ]]; then
  CI_MODE=true
  echo "Running in CI mode - will skip commit operations"
fi

latest_version=$(curl -Is "https://github.com/linux-pam/linux-pam/releases/latest" | grep "location" | head -1 | sed "s#.*tag/v##g" | tr -d "\r")
echo "Latest Linux PAM version: v${latest_version}"

sed -i "s/^pkgver=.*$/pkgver=${latest_version}/" ./PKGBUILD

if ! git diff --quiet HEAD PKGBUILD; then

  if pacman -Qi pacman-contrib > /dev/null 2>&1; then
    updpkgsums
  else
    echo "Install pacman-contrib with 'pacman -S pacman-contrib'"
    exit 1
  fi

  makepkg --printsrcinfo > .SRCINFO

  makepkg -si

  if [ "$CI_MODE" = false ]; then
    # Only commit if not in CI mode
    git add PKGBUILD .SRCINFO
    git commit -m "Updated version to ${latest_version}"
    git push origin master
  else
    echo "Skipping commit in CI mode"
  fi
else
  echo "No updates found!"
fi
