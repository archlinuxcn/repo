# Maintainer: graysky <graysky AT archlinux DOT us>

pkgname=kodi-standalone-service
pkgver=1.135
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
b2sums=('ff734b461a2d1e71f9a4026345800d51d3cb48ecc09beb9bf6917211cfbe4de4342c7746453fe93ad012917c25a3d5de54b21c4de24fec0ac5fbcb507ce99e88')

package() {
  cd "$pkgname-$pkgver"
  make
  make DESTDIR="$pkgdir" install
}

# vim:set ts=2 sw=2 et:
