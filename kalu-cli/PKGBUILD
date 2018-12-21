# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>
# This package is forked from aur/kalu. Original contributors are:
# Contributor: jjacky

_pkgname=kalu
pkgname=$_pkgname-cli
pkgver=4.3.0
pkgrel=4
pkgdesc="Upgrade notifier w/ AUR support, watched (AUR) packages, news (CLI only)"
arch=('i686' 'x86_64')
url="https://jjacky.com/kalu"
license=('GPL3+')
depends=('pacman>=5.1' 'pacman<5.2' 'curl' 'glib2')
source=(https://jjacky.com/$_pkgname/$_pkgname-$pkgver.tar.xz)
sha256sums=('83c886e832c29768b0b80e0ee463ca057eae1a3511d2b8babdc8d6347f02cb5a')
conflicts=("$_pkgname")

build() {
  cd $_pkgname-$pkgver
  ./configure --prefix=/usr --disable-gui
  make
}

package() {
  cd $_pkgname-$pkgver
  make DESTDIR="$pkgdir" install
}

# vim:set ts=2 sw=2 et:
