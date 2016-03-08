# Author: Julien MISCHKOWITZ <wain@archlinux.fr>
# Author: tuxce <tuxce.net@gmail.com>
# Contributor: Skunnyk <skunnyk@archlinux.fr>

pkgname=yaourt
pkgver=1.8.1
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
source=("$url/releases/download/$pkgver/$pkgname-$pkgver.tar.xz")
sha256sums=('f5da1144f2d4e9754bc5728116a79a9c78469f6587321c4c766812f06393ca92')

build() {
  cd "$srcdir/$pkgname-$pkgver/"
  make PREFIX=/usr sysconfdir=/etc localstatedir=/var
}

package() {
  cd "$srcdir/$pkgname-$pkgver/"
  make PREFIX=/usr sysconfdir=/etc localstatedir=/var DESTDIR="$pkgdir" install
}

# vim:set ts=2 sw=2 et:
