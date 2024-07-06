# Maintainer: graysky <therealgraysky AT protonmail DOT com>

pkgname=kodi-standalone-service
pkgver=1.137
pkgrel=2
pkgdesc="Systemd services to run kodi in stand-alone mode without a DE"
# This is only for x86_64
# The kodi-rpi packages for ArchARM provide their own versions of this package
arch=(x86_64)
url="https://github.com/graysky2/kodi-standalone-service"
license=(MIT)
install=readme.install
depends=(polkit kodi)
replaces=(kodi-standalone-x11-service kodi-standalone-gbm-service kodi-standalone-wayland-service)
backup=(etc/conf.d/kodi-standalone)
optdepends=(
 'cage: for kodi-wayland.service'
 'wayland: for kodi-wayland.service'
 'xorg-server: for kodi-x11.service'
 'xorg-xinit: for kodi-x11.service'
) 
source=("$pkgname-v$pkgver.tar.gz::https://github.com/graysky2/$pkgname/archive/v$pkgver.tar.gz")
b2sums=('7ba4612bd089103b78bdf04838f150c2be023b7ccd9814b9d5d3b2d37a266e0db2a1cbc378254a5ba2c98de5f58193b0acf22c5ac104f91f1c9b614624177610')

package() {
  cd "$pkgname-$pkgver"
  make
  make DESTDIR="$pkgdir" install
}

# vim:set ts=2 sw=2 et:
