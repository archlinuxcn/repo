# Maintainer: Steffen Weber <-boenki-gmx-de->
# Contributor: kfgz <kfgz at interia pl>
# Contributor: Thayer Williams <thayer at archlinux dot org>
# Contributor: James Rayner <james at archlinux dot org>
# Contributor: William Rea <sillywilly at gmail dot com>

pkgname=tango-icon-theme-extras
pkgver=0.1.0
pkgrel=7
pkgdesc="Extra icons for Tango"
arch=('any')
url="http://tango.freedesktop.org"
license=('CCPL:by-sa')
depends=('tango-icon-theme')
makedepends=('imagemagick' 'icon-naming-utils')
options=(!strip !zipman)
source=(${url}/releases/${pkgname}-${pkgver}.tar.gz
        rsvg.patch)
md5sums=('caaceaec7b61f1cbda0db9842f9db281'
         '05a5734cfe49605006a1fc3fb5fca095')

prepare() {
  cd ${pkgname}-${pkgver}
  patch -p0 < "${srcdir}/rsvg.patch"
  autoreconf -fi
}

build() {
  cd ${pkgname}-${pkgver}
  ./configure --prefix=/usr --enable-png-creation
  make
}

package() {
  cd ${pkgname}-${pkgver}
  make DESTDIR="${pkgdir}" install
}
