# Maintainer: Clément Démoulins <clement@archivel.fr>

pkgname=pamixer
pkgver=1.3
pkgrel=2
pkgdesc="Pulseaudio command-line mixer like amixer"
arch=('i686' 'x86_64')
url="https://github.com/cdemoulins/pamixer"
license=('GPL3')
conflicts=('pamixer-git')
replaces=('pamixer-git')
depends=('libpulse' 'boost-libs')
makedepends=('boost')

source=(https://github.com/cdemoulins/${pkgname}/archive/${pkgver}.tar.gz)
md5sums=('c43b97a565edcaee3161641416108355')

build() {
  cd "$srcdir/${pkgname}-${pkgver}"
  make
}

package() {
  cd "$srcdir/${pkgname}-${pkgver}"
  install -D -m755 pamixer $pkgdir/usr/bin/pamixer
}

# vim:set ts=2 sw=2 et:
