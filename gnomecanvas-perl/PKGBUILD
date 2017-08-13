# $Id$
# Maintainer: PhotonX <photon89@googlemail.com>
# Contributor: Jan de Groot <jgc@archlinux.org>

pkgname=gnomecanvas-perl
_realname=Gnome2-Canvas
pkgver=1.002
pkgrel=18
pkgdesc="Gnome2-Canvas perl bindings for libgnomecanvas"
arch=('i686' 'x86_64')
license=('LGPL')
url="http://gtk2-perl.sourceforge.net/"
makedepends=('perl-extutils-pkgconfig' 'perl-extutils-depends')
depends=('gtk2-perl' 'libgnomecanvas' 'perl')
options=(!emptydirs)
source=(http://downloads.sourceforge.net/sourceforge/gtk2-perl/${_realname}-${pkgver}.tar.gz)
md5sums=('93405a987ba4bbd03c2f91592b88f5cb')

build() {
  cd "${srcdir}/${_realname}-${pkgver}"
  PERL_MM_USE_DEFAULT=1 perl Makefile.PL INSTALLDIRS=vendor 
  PERL_USE_UNSAFE_INC=1 make
}

package() {
  cd "${srcdir}/${_realname}-${pkgver}"
  make install DESTDIR="${pkgdir}"
}
