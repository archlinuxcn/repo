# Author: Julien MISCHKOWITZ <wain@archlinux.fr>
# Author: tuxce <tuxce.net@gmail.com>
# Contributor: Skunnyk <skunnyk@archlinux.fr>

pkgname=yaourt
pkgver=1.9
pkgrel=1
pkgdesc="A pacman wrapper with extended features and AUR support"
arch=('any')
url="https://github.com/archlinuxfr/$pkgname"
license=(GPL)
depends=('diffutils' 'pacman>=5.0' 'package-query>=1.8' 'gettext')
optdepends=('aurvote: vote for favorite packages from AUR'
            'customizepkg: automatically modify PKGBUILD during install/upgrade'
            'rsync: retrieve PKGBUILD from official repositories')
backup=('etc/yaourtrc')
source=("$url/releases/download/$pkgver/$pkgname-$pkgver.tar.gz")
sha256sums=('9a485cef9d50e80b8abae5dbb147e09bdeb8818d29316b65e892fb560c48517d')

build() {
  cd "$srcdir/$pkgname-$pkgver/"
  make PREFIX=/usr sysconfdir=/etc localstatedir=/var
}

package() {
  cd "$srcdir/$pkgname-$pkgver/"
  make PREFIX=/usr sysconfdir=/etc localstatedir=/var DESTDIR="$pkgdir" install
}

# vim:set ts=2 sw=2 et:
