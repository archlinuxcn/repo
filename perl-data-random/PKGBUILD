# Maintainer:  Michael Kogan <michael dot kogan at gmx dot net>

pkgname=perl-data-random
pkgver=0.11
pkgrel=1
pkgdesc="Data::Random - Perl module to generate random data"
arch=('i686' 'x86_64')
url="http://search.cpan.org/~barefoot/Data-Random/lib/Data/Random.pm"
license=('GPL, PerlArtistic')
depends=('perl-date-calc' 'perl-gd' 'perl-yaml-tiny')
source=(http://ftp.gwdg.de/pub/languages/perl/CPAN/authors/id/B/BA/BAREFOOT/Data-Random-${pkgver}.tar.gz)
md5sums=('9604ddc45eff8fc95803f34a7553c93b')

build() {
    cd "$srcdir/Data-Random-${pkgver}"
    perl Makefile.PL INSTALLDIRS=vendor
    make || return 1
}
package() {
    cd "$srcdir/Data-Random-${pkgver}"
    make DESTDIR=$pkgdir install || return 1
}
