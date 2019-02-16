# Maintainer: Stefan Husmann <stefan-husmann@t-online.de>

pkgname=perl-cpanel-json-xs
pkgver=4.09
pkgrel=1
pkgdesc="cPanel fork of JSON::XS, fast and correct serializing"
arch=('i686' 'x86_64')
license=('PerlArtistic' 'GPL')
options=('!emptydirs')
depends=('perl')
url='https://metacpan.org/release/Cpanel-JSON-XS'
source=("https://cpan.metacpan.org/authors/id/R/RU/RURBAN/Cpanel-JSON-XS-$pkgver.tar.gz")
sha512sums=('9d0771129a473b696bcfd502303a88e8e97f0dc2cf2b97003328edf72182400b8c07a2f5cf120f102c32a04118d4530f3d7da369c9b063554d2cfc0feddbb6aa')
_distdir="Cpanel-JSON-XS-$pkgver"

build() {
  export PERL_MM_USE_DEFAULT=1 PERL5LIB=""                 \
	 PERL_AUTOINSTALL=--skipdeps                            \
	 PERL_MM_OPT="INSTALLDIRS=vendor DESTDIR='$pkgdir'"     \
	 PERL_MB_OPT="--installdirs vendor --destdir '$pkgdir'" \
	 MODULEBUILDRC=/dev/null
  
  cd "$_distdir"
  /usr/bin/perl Makefile.PL
  make
}

check() {
  cd "$_distdir"
  export PERL_MM_USE_DEFAULT=1 PERL5LIB=""
  make test
}

package() {
  cd "$_distdir"
  make install 
  find "$pkgdir" -name .packlist -o -name perllocal.pod -delete
}
