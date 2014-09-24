# Maintainer: lilydjwg <lilydjwg@gmail.com>
pkgname=fbcat
pkgver=0.4
pkgrel=1
pkgdesc="A framebuffer screenshot grabber"
arch=(i686 x86_64)
url="http://code.google.com/p/fbcat/"
license=("GPLv2")
optdepends=('imagemagick: for fbgrab' 'netpbm: for fbgrab' 'graphicsmagick: for fbgrab')
makedepends=('docbook-xsl')
source=(https://bitbucket.org/jwilk/${pkgname}/downloads/${pkgname}-${pkgver}.tar.gz)
conflicts=('fbgrab')
md5sums=('7ae033c7fb3c0624d501c4ce7e06ab4b')

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
  install -D -m644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}/COPYING"
}
# vim:syntax=sh
