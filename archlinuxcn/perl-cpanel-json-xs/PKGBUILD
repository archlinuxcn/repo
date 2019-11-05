# Contributor: ordoban <dirk.langer@vvovgonik.de>
# Generator  : CPANPLUS::Dist::Arch 1.32

pkgname='perl-cpanel-json-xs'
pkgver='4.16'
pkgrel='1'
pkgdesc="cPanel fork of JSON::XS, fast and correct serializing"
arch=('i686' 'x86_64')
license=('PerlArtistic' 'GPL')
options=('!emptydirs')
depends=('perl>=0')
makedepends=()
url='https://metacpan.org/release/Cpanel-JSON-XS'
source=('https://cpan.metacpan.org/authors/id/R/RU/RURBAN/Cpanel-JSON-XS-4.16.tar.gz')
md5sums=('80cf1a310cf2dfa2000e3c7ab2dc2905')
sha512sums=('28ea6ed6b6e275b22c92f2a1c01b13fe8cd9ebe1443eef1caf4773a9ec7c60eb2c13504d33101751881184bf8f0de4ff5c1cee469f569ce900e0bf3b3c654b00')
_distdir="Cpanel-JSON-XS-4.16"

build() {
  export PERL_MM_USE_DEFAULT=1 PERL5LIB=""                      \
         PERL_AUTOINSTALL=--skipdeps                            \
         PERL_MM_OPT="INSTALLDIRS=vendor DESTDIR='$pkgdir'"     \
         PERL_MB_OPT="--installdirs vendor --destdir '$pkgdir'" \
         MODULEBUILDRC=/dev/null

  cd "$srcdir/$_distdir"
  /usr/bin/perl Makefile.PL
  make
}

check() {
  cd "$srcdir/$_distdir"
  export PERL_MM_USE_DEFAULT=1 PERL5LIB="."
  make test
}

package() {
  cd "$srcdir/$_distdir"
  make install

  find "$pkgdir" \( -name .packlist -o -name perllocal.pod \) -delete
}

# Local Variables:
# mode: shell-script
# sh-basic-offset: 2
# End:
# vim:set ts=2 sw=2 et:
