# Contributor: John D Jones III <jnbek1972 -_AT_- g m a i l -_Dot_- com>
# Generator  : CPANPLUS::Dist::Arch 1.28

pkgname='perl-proc-simple'
pkgver='1.31'
pkgrel='3'
pkgdesc="launch and control background processes"
arch=('any')
license=('PerlArtistic' 'GPL')
options=('!emptydirs')
depends=('perl')
makedepends=()
url='http://search.mcpan.org/dist/Proc-Simple'
source=('http://search.mcpan.org/CPAN/authors/id/M/MS/MSCHILLI/Proc-Simple-1.31.tar.gz')
md5sums=('46f36d79dc76d10f9a44928b9e61817e')
sha512sums=('0000011949b9c725f2af18f02bddbcfa1e70edea4be7a1d730ac3dd8a4335e658e4852db1230180fb27ee86144d0b0eb57ac6bb1fbca72952960cd9e0abd3b8a')
_distdir="Proc-Simple-1.31"

build() {
  ( export PERL_MM_USE_DEFAULT=1 PERL5LIB=""                 \
      PERL_AUTOINSTALL=--skipdeps                            \
      PERL_MM_OPT="INSTALLDIRS=vendor DESTDIR='$pkgdir'"     \
      PERL_MB_OPT="--installdirs vendor --destdir '$pkgdir'" \
      MODULEBUILDRC=/dev/null

    cd "$srcdir/$_distdir"
    /usr/bin/perl Makefile.PL
    make
  )
}

check() {
  cd "$srcdir/$_distdir"
  ( export PERL_MM_USE_DEFAULT=1 PERL5LIB=""
    make test
  )
}

package() {
  cd "$srcdir/$_distdir"
  make install

  find "$pkgdir" -name .packlist -o -name perllocal.pod -delete
}

# Local Variables:
# mode: shell-script
# sh-basic-offset: 2
# End:
# vim:set ts=2 sw=2 et:
