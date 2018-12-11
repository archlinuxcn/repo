# Maintainer: Stefan Husmann <stefan-husmann@t-online.de>

pkgname=perl-cpanel-json-xs
pkgver=4.08
pkgrel=1
pkgdesc="cPanel fork of JSON::XS, fast and correct serializing"
arch=('i686' 'x86_64')
license=('PerlArtistic' 'GPL')
options=('!emptydirs')
depends=('perl')
url='https://metacpan.org/release/Cpanel-JSON-XS'
source=("https://cpan.metacpan.org/authors/id/R/RU/RURBAN/Cpanel-JSON-XS-$pkgver.tar.gz")
sha512sums=('7236923791b244e022cea00f3c8697905a8187edddaf0b197ee6f8a4afe958c42ea37f655e0db8e4c66a07427b7888e68ae1dc08849ef7cbb518155b2d9c65f5')
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
