# Contributor: John D Jones III <j[nospace]n[nospace]b[nospace]e[nospace]k[nospace]1972 -_AT_- the domain name google offers a mail service at ending in dot com>
# Generator  : CPANPLUS::Dist::Arch 1.28

pkgname='perl-devel-checkcompiler'
pkgver='0.05'
pkgrel='1'
pkgdesc="Check the compiler's availability"
arch=('any')
license=('PerlArtistic' 'GPL')
options=('!emptydirs')
depends=('perl>=5.8.1')
makedepends=()
checkdepends=('perl-test-requires>=0')
url='http://search.cpan.org/dist/Devel-CheckCompiler'
source=('http://search.cpan.org/CPAN/authors/id/S/SY/SYOHEX/Devel-CheckCompiler-0.05.tar.gz')
md5sums=('c100463971b68f4125062447648eb82d')
sha512sums=('5bf40abc7df914a9bbd5b185a40d597272f2f8fb0a94f95b1790ed247a529af8c31bc8ddfcae75ceab4d504ad8faf86ed63eefbc5081a208bcccf0902464d73e')
_distdir="Devel-CheckCompiler-0.05"

build() {
  ( export PERL_MM_USE_DEFAULT=1 PERL5LIB=""                 \
      PERL_AUTOINSTALL=--skipdeps                            \
      PERL_MM_OPT="INSTALLDIRS=vendor DESTDIR='$pkgdir'"     \
      PERL_MB_OPT="--installdirs vendor --destdir '$pkgdir'" \
      MODULEBUILDRC=/dev/null

    cd "$srcdir/$_distdir"
    /usr/bin/perl Build.PL
    /usr/bin/perl Build
  )
}

check() {
  cd "$srcdir/$_distdir"
  ( export PERL_MM_USE_DEFAULT=1 PERL5LIB=""
    /usr/bin/perl Build test
  )
}

package() {
  cd "$srcdir/$_distdir"
  /usr/bin/perl Build install

  find "$pkgdir" -name .packlist -o -name perllocal.pod -delete
}

# Local Variables:
# mode: shell-script
# sh-basic-offset: 2
# End:
# vim:set ts=2 sw=2 et:
