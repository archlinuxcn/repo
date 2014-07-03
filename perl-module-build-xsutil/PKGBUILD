# Contributor: John D Jones III <j[nospace]n[nospace]b[nospace]e[nospace]k[nospace]1972 -_AT_- the domain name google offers a mail service at ending in dot com>
# Generator  : CPANPLUS::Dist::Arch 1.28

pkgname='perl-module-build-xsutil'
pkgver='0.06'
pkgrel='2'
pkgdesc="A Module::Build class for building XS modules"
arch=('any')
license=('PerlArtistic' 'GPL')
options=('!emptydirs')
depends=('perl-devel-checkcompiler>=0.02' 'perl' 'perl-module-build>=0.4205')
makedepends=()
url='http://search.cpan.org/dist/Module-Build-XSUtil'
source=('http://search.cpan.org/CPAN/authors/id/H/HI/HIDEAKIO/Module-Build-XSUtil-0.06.tar.gz')
md5sums=('1af74043aa7593cf949832472090c796')
sha512sums=('4e88cde2369209546a8d0a1e7c4d65234abb6be284e5d4cc63b0cebb94a4fec33a42023d8faedb105e9e1e103f8e5bfd9ee5769c1b7108ea6b9af83509dbe640')
_distdir="Module-Build-XSUtil-0.06"

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
