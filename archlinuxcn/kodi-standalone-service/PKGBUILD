# Maintainer: graysky <therealgraysky AT protonmail DOT com>

pkgname=kodi-standalone-service
pkgver=1.136
pkgrel=1
pkgdesc="Systemd services to run kodi in stand-alone mode without a DE"
# Do NOT attempt to use this package on Arch ARM! This is only for x86_64.
# You have been warned.
arch=(x86_64)
url="https://github.com/graysky2/kodi-standalone-service"
license=(MIT)
install=readme.install
depends=(polkit kodi)
replaces=(kodi-standalone-x11-service kodi-standalone-gbm-service kodi-standalone-wayland-service)
backup=(etc/conf.d/kodi-standalone)
optdepends=(
 'cage: for kodi-wayland.service'
 'xorg-server: for kodi-x11.service'
 'xorg-xinit: for kodi-x11.service'
 'xorg-xwayland: for kodi-wayland.service'
) 
source=("$pkgname-v$pkgver.tar.gz::https://github.com/graysky2/$pkgname/archive/v$pkgver.tar.gz")
b2sums=('be6c287dcc88041310cf1859ce39457a320a68f84ff3c7f981e36ecc2bc4540140c254e60738bbd96c9be39800360382c5eeaf69c4b6e7f1fa15fdf705927ff4')

package() {
  cd "$pkgname-$pkgver"
  make
  make DESTDIR="$pkgdir" install
}

# vim:set ts=2 sw=2 et:
