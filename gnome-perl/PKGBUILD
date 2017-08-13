# $Id$
# Maintainer: PhotonX <photon89@googlemail.com>
# Contributor: Jan de Groot <jgc@archlinux.org>

pkgname=gnome-perl
pkgver=1.045
pkgrel=8
pkgdesc="Perl bindings for libgnome"
arch=('i686' 'x86_64')
license=('LGPL')
url="http://gtk2-perl.sourceforge.net/"
makedepends=('perl-extutils-pkgconfig' 'perl-extutils-depends')
depends=('gnomecanvas-perl' 'gnome-vfs-perl' 'libgnomeui' 'perl')
options=('!emptydirs')
source=(http://downloads.sourceforge.net/sourceforge/gtk2-perl/Gnome2-${pkgver}.tar.gz)
md5sums=('95c06139f9d950df17c9cb0340c74168')

build() {
  cd Gnome2-$pkgver
  perl Makefile.PL INSTALLDIRS=vendor
  PERL_USE_UNSAFE_INC=1 make
}

package() {
  cd Gnome2-$pkgver
  make DESTDIR="${pkgdir}" install
}
