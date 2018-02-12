# $Id$
# Maintainer: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Maintainer: Vesa Kaihlavirta <vegai@iki.fi>
# Contributor: Sebastian Sareyko <public@nooms.de>

pkgname=gnustep-base
pkgver=1.25.1
pkgrel=1
pkgdesc="The GNUstep base package"
arch=('x86_64')
url="http://www.gnustep.org/"
license=("GPL" "LGPL")
depends=(libxslt avahi gmp gcc-libs openssl libffi gnustep-make gnutls icu)
makedepends=(gcc-objc)
conflicts=('gnustep-base-svn')
groups=('gnustep-core')
options=('!emptydirs' '!makeflags')
source=(https://github.com/gnustep/libs-base/releases/download/base-${pkgver//./_}/gnustep-base-${pkgver}.tar.gz{,.sig})
sha256sums=('f28beb9ca485674bcce3053896ad90a31b109fb97c5a041827c72f241e8db69e'
            'SKIP')
validpgpkeys=('83AAE47CE829A4146EF83420CA868D4C99149679')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  source /usr/share/GNUstep/Makefiles/GNUstep.sh
  ./configure --prefix=/usr --sysconfdir=/etc/GNUstep \
	--with-ffi-include=/usr/lib/libffi-`pacman -Q libffi | cut -f2 -d\ |cut -f1 -d-`/include/
  # fix file ownership
  sed -i 's/tar -xf $(TIMEZONE_ARCHIVE);/tar -xf $(TIMEZONE_ARCHIVE);chown -R root:root * ;/' NSTimeZones/Makefile.postamble
  sed -i 's|.*gnutls_transport_set_lowat.*||' Source/GSSocketStream.m
  make VERBOSE=1
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make DESTDIR="$pkgdir" install
  chown -R root.root "$pkgdir/"
}
