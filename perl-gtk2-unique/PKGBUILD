# Maintainer: Brian Bidulock <bidulock@openss7.org>

pkgname=perl-gtk2-unique
_realname=Gtk2-Unique
pkgver=0.05
pkgrel=9
pkgdesc="Perl bindings for the C library libunique"
arch=('i686' 'x86_64')
url="https://metacpan.org/release/${_realname}"
license=('LGPL' 'PerlArtistic')
makedepends=('perl-extutils-depends' 'perl-extutils-pkgconfig')
depends=('gtk2-perl' 'libunique')
options=('!emptydirs')
source=(http://search.cpan.org/CPAN/authors/id/P/PO/POTYL/${_realname}-${pkgver}.tar.gz
	$pkgname.patch)
md5sums=('0beb552933b765a017588563a71af123'
         'f8e15e1b93e2629e1745f8e4de8524ff')

build() {
  cd  "$srcdir/$_realname-$pkgver"
  patch -Np1 -i "$srcdir/$pkgname.patch"
  PERL_MM_USE_DEFAULT=1 perl Makefile.PL INSTALLDIRS=vendor
  make
}
package() {
  cd  "$srcdir/$_realname-$pkgver"
  make install DESTDIR=$pkgdir
  find $pkgdir -name '.packlist' -delete
  find $pkgdir -name '*.pod' -delete
}
