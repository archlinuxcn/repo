# Maintainer: Stefan Husmann <stefan-husmann@t-online.de>

pkgname=perl-cpanel-json-xs
pkgver=4.10
pkgrel=1
pkgdesc="cPanel fork of JSON::XS, fast and correct serializing"
arch=('i686' 'x86_64')
license=('PerlArtistic' 'GPL')
options=('!emptydirs')
depends=('perl')
url='https://metacpan.org/release/Cpanel-JSON-XS'
source=("https://cpan.metacpan.org/authors/id/R/RU/RURBAN/Cpanel-JSON-XS-$pkgver.tar.gz")
sha512sums=('ffc7804200b904fac34784763c768c552d19cb1b39d556ec5ca19a88eaa53bb0ea929702eabe2f3f49f175253135b55a6e509606eb3f2421925b0266df6b96bb')
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
