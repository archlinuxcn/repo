# Maintainer: Stefan Husmann <stefan-husmann@t-online.de>

pkgname=perl-cpanel-json-xs
pkgver=4.11
pkgrel=1
pkgdesc="cPanel fork of JSON::XS, fast and correct serializing"
arch=('i686' 'x86_64')
license=('PerlArtistic' 'GPL')
options=('!emptydirs')
depends=('perl')
url='https://metacpan.org/release/Cpanel-JSON-XS'
source=("https://cpan.metacpan.org/authors/id/R/RU/RURBAN/Cpanel-JSON-XS-$pkgver.tar.gz")
sha512sums=('a14fe211b769184c28d946b9e88d9a380331d6a16c67a0f286fb4bf0f25e2a3b80f3df907bdf1a7eceaa8a34e69f13b3296cc135bc1ea2d2fcba6355dcf88579')
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
