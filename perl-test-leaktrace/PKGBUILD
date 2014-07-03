# Contributor: John D Jones III <j[nospace]n[nospace]b[nospace]e[nospace]k[nospace]1972 -_AT_- the domain name google offers a mail service at ending in dot com>
# Generator  : CPANPLUS::Dist::Arch 1.25

pkgname='perl-test-leaktrace'
pkgver='0.14'
pkgrel='1'
pkgdesc="Traces memory leaks"
arch=('i686' 'x86_64')
license=('PerlArtistic' 'GPL')
options=('!emptydirs')
depends=('perl>=5.8.1')
makedepends=()
url='http://search.cpan.org/dist/Test-LeakTrace'
source=('http://search.cpan.org/CPAN/authors/id/G/GF/GFUJI/Test-LeakTrace-0.14.tar.gz')
md5sums=('d53953f442cf782c30f843df677db210')
sha512sums=('1bbd77bc2bc081a51b1f9fc946ece08bc5266efa41ac52d7216622b56ab2b122b419fdc0ba9f6a329eb506d6be56711b823310ef71b3171da0e13d4d3a8497d1')
_distdir="Test-LeakTrace-0.14"

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
