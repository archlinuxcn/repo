# Contributor: ordoban <dirk.langer@vvovgonik.de>
# Generator  : CPANPLUS::Dist::Arch 1.32

pkgname='perl-cpanel-json-xs'
pkgver='4.13'
pkgrel='1'
pkgdesc="cPanel fork of JSON::XS, fast and correct serializing"
arch=('i686' 'x86_64')
license=('PerlArtistic' 'GPL')
options=('!emptydirs')
depends=('perl>=0')
makedepends=()
url='https://metacpan.org/release/Cpanel-JSON-XS'
source=('https://cpan.metacpan.org/authors/id/R/RU/RURBAN/Cpanel-JSON-XS-4.13.tar.gz')
md5sums=('bc9388603988d5e55dab2cf9f618fbd8')
sha512sums=('02aeda7488fd4fc4309502a2df14f515c2f02be4e1de62c0a67af81c486d8a820a81d4f23f1d6060a3b0265556ea96ba4d43ba47c2c8dc99ca68d511123b7196')
_distdir="Cpanel-JSON-XS-4.13"

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
