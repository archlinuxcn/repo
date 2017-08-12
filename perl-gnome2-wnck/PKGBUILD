# $Id: PKGBUILD 194152 2016-10-31 13:48:24Z spupykin $
# Maintainer: Crotok <crotok [at] mailbox [dot] org>
# Contributor: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: Alessio 'mOLOk' Bolognino <themolok@gmail.com>

pkgname=perl-gnome2-wnck
pkgver=0.16
pkgrel=15
pkgdesc="Perl interface to the Window Navigator Construction Kit"
arch=('i686' 'x86_64')
license=("GPL" "PerlArtistic")
url="http://search.cpan.org/dist/Gnome2-Wnck"
depends=('perl' 'gtk2-perl' 'libwnck')
makedepends=('perl-extutils-depends' 'perl-extutils-pkgconfig')
options=('!emptydirs')
source=("http://search.cpan.org/CPAN/authors/id/T/TS/TSCH/Gnome2-Wnck-${pkgver}.tar.gz")
md5sums=('439f4569ffd7af96ef1d3feaab23760e')

build() {
  cd Gnome2-Wnck-${pkgver}
  export PERL_MM_USE_DEFAULT=1 PERL_USE_UNSAFE_INC=1
  perl Makefile.PL INSTALLDIRS=vendor
  make
}

package() {
  cd Gnome2-Wnck-${pkgver}
  make install DESTDIR="$pkgdir"
}
