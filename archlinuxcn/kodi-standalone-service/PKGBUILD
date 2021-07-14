# Maintainer: graysky <graysky AT archlinux DOT us>

pkgname=kodi-standalone-service
pkgver=1.131
pkgrel=1
pkgdesc="Systemd services to run kodi in stand-alone mode without a DE"
# Do NOT attempt to use this package on Arch ARM! This is only for x86_64.
# You have been warned.
arch=('x86_64')
url="https://github.com/graysky2/kodi-standalone-service"
license=('MIT')
install=readme.install
depends=('polkit' 'libinput')
replaces=('kodi-standalone-x11-service' 'kodi-standalone-gbm-service' 'kodi-standalone-wayland-service')
optdepends=(
 'cage: for kodi-wayland.service'
 'xorg-server: for kodi-x11.service'
 'xorg-xinit: for kodi-x11.service'
) 
source=("$pkgname-v$pkgver.tar.gz::https://github.com/graysky2/$pkgname/archive/v$pkgver.tar.gz")
b2sums=('014a6972075899e65b75ed606692568c41b190635873b3c3cae6bb03eefc295671e440b23e97638fa4ada26e1ae1038a8534ba8fbed730c85c8384acf2dc73bb')

package() {
  cd "$pkgname-$pkgver"
  make
  make DESTDIR="$pkgdir" install
}

# vim:set ts=2 sw=2 et:
