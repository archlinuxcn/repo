# Maintainer: Colin Keenan <colinnkeenan at gmail dot com>

# After installing this package (nautilus-data), you can get gnome-search-tool for Xfce without nautilus/gnome-desktop.
# 
# Either install gnome-search-tool-no-nautilus from AUR, 
# or
# use abs as follows: 
# 
# sudo abs extra/gnome-search-tool
# mkdir ~/abs
# cp -r /var/abs/extra/gnome-search-tool/ ~/abs
# cd ~/abs/gnome-search-tool 
# [edit PKGBUILD and change depends=('nautilus' ...) to depends=('nautilus-data' ...)] 
# makepkg -si
# 
# The advantage of gnome-search-tool-no-nautilus from AUR over rebuilding with abs is that upgrades will be easier.

pkgname=nautilus-data
pkgver=3.10.1
pkgrel=8
pkgdesc="Nautilus data files for gnome-search-tool"
url="http://www.ubuntuupdates.org/package/core/trusty/main/base/nautilus-data"
arch=('any')
license=('GPL')
conflicts=('nautilus')
install=${pkgname}.install

source=(http://security.ubuntu.com/ubuntu/pool/main/n/nautilus/nautilus-data_3.10.1-0ubuntu8_all.deb)
md5sums=('e556bc3656a69dcdbf6cd39276941ff1')

package() {
  msg2 "Extracting the data.tar.xz"
  tar xvf data.tar.xz -C "$pkgdir"
}
