#!/usr/bin/env bash

#
# This script is called by build.sh and actually does the AUR build inside a Docker container.
# It is not used in the AUR builds in any way, and is only for debugging purposes.
#

set -e

pacman -Sy --noconfirm
pacman -S git --noconfirm
echo 'yay ALL=(ALL:ALL) NOPASSWD: ALL' >> /etc/sudoers
useradd -d /home/yay -g users -m -s /bin/bash yay
cd /tmp
sudo -u yay git clone https://aur.archlinux.org/yay-bin.git
cd /tmp/yay-bin
sudo -u yay makepkg -si --noconfirm
sudo -u yay yay -S --noconfirm ferdium
cp /home/yay/.cache/yay/ferdium/ferdium-*.pkg.tar.zst /tmp/output
