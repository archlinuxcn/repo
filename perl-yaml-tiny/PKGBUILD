# Contributor: AUR Perl <aurperl@juster.info>
# Generator  : CPANPLUS::Dist::Arch 1.15

pkgname='perl-yaml-tiny'
pkgver='1.62'
pkgrel='1'
pkgdesc="Read/Write YAML files with as little code as possible"
arch=('any')
license=('PerlArtistic' 'GPL')
options=('!emptydirs')
depends=('perl>=5.004')
makedepends=('perl-module-build-tiny' 'perl-test-harness')
url='http://search.cpan.org/dist/YAML-Tiny'
source=('http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/YAML-Tiny-1.62.tar.gz')
md5sums=('1308d3244d1b27088b4c101bf9705e9d')

build() {
  ( export PERL_MM_USE_DEFAULT=1 PERL5LIB=""                 \
      PERL_AUTOINSTALL=--skipdeps                            \
      PERL_MM_OPT="INSTALLDIRS=vendor DESTDIR='$pkgdir'"     \
      PERL_MB_OPT="--installdirs vendor --destdir '$pkgdir'" \
      MODULEBUILDRC=/dev/null

    cd "${srcdir}/YAML-Tiny-${pkgver}"
    /usr/bin/perl Build.PL
    ./Build
  )
}

package() {
  cd "${srcdir}/YAML-Tiny-${pkgver}"
  ./Build install
  find "$pkgdir" -name .packlist -o -name perllocal.pod -delete
}

# Local Variables:
# mode: shell-script
# sh-basic-offset: 2
# End:
# vim:set ts=2 sw=2 et:
