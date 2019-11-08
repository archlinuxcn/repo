# Maintainer: lilydjwg <lilydjwg@gmail.com>
pkgname=fbcat
pkgver=0.5.1
pkgrel=3
pkgdesc="A framebuffer screenshot grabber"
arch=(i686 x86_64)
url="https://github.com/jwilk/fbcat"
license=("GPLv2")
optdepends=('imagemagick: for fbgrab' 'netpbm: for fbgrab' 'graphicsmagick: for fbgrab')
makedepends=('docbook-xsl')
source=(https://github.com/jwilk/${pkgname}/releases/download/${pkgver}/${pkgname}-${pkgver}.tar.gz)
conflicts=('fbgrab')
md5sums=('944fd3854bfe00971bfcd830f6c94497')

build() {
  cd $srcdir/${pkgname}-${pkgver}
  make
  (cd doc && make)
}
package() {
  cd $srcdir/${pkgname}-${pkgver}
  install -D -m755 fbcat ${pkgdir}/usr/bin/fbcat
  install -D -m755 fbgrab ${pkgdir}/usr/bin/fbgrab
  install -D -m644 doc/fbcat.1 ${pkgdir}/usr/share/man/man1/fbcat.1
  install -D -m644 doc/fbgrab.1 ${pkgdir}/usr/share/man/man1/fbgrab.1
}
# vim:syntax=sh
