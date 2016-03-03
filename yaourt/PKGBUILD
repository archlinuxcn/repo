# Author: Julien MISCHKOWITZ <wain@archlinux.fr>
# Author: tuxce <tuxce.net@gmail.com>
# Contributor: Skunnyk <skunnyk@archlinux.fr>

pkgname=yaourt
pkgver=1.8
pkgrel=1
pkgdesc="A pacman wrapper with extended features and AUR support"
arch=('any')
url="https://github.com/archlinuxfr/yaourt"
license=(GPL)
depends=('diffutils' 'pacman>=5.0' 'package-query>=1.8' 'gettext')
optdepends=('aurvote: vote for favorite packages from AUR'
      'customizepkg: automatically modify PKGBUILD during install/upgrade'
      'rsync: retrieve PKGBUILD from official repositories')
backup=('etc/yaourtrc')
source=(http://mir.archlinux.fr/releases/$pkgname/$pkgname-$pkgver.tar.gz)

build() { 
  cd "$srcdir/$pkgname-$pkgver/"
  make PREFIX=/usr sysconfdir=/etc localstatedir=/var 
}

package() {
  cd "$srcdir/$pkgname-$pkgver/"
  make PREFIX=/usr sysconfdir=/etc localstatedir=/var DESTDIR="$pkgdir" install
}

# vim:set ts=2 sw=2 et:
sha256sums=('251a371d40906d235fd8a8f49b00b35ccd56e8d36c1eb53790d216ac986b71bf')
