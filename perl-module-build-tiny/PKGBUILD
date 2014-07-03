# Contributor: xRemaLx <anton.komolov@gmail.com>

pkgname='perl-module-build-tiny'
_pkgname='Module-Build-Tiny'
pkgver='0.036'
pkgrel='1'
pkgdesc="A tiny replacement for Module::Build"
arch=('any')
license=('PerlArtistic' 'GPL')
options=('!emptydirs')
depends=('perl>=5.8.1' 'perl-extutils-config>=0.003' 'perl-extutils-helpers>=0.020' 'perl-extutils-installpaths>=0.002')
makedepends=('perl-test-harness>=3.29')
provides=("module-build-tiny=${pkgver}" "Module::Build::Tiny=${pkgver}" "perl-module-build-tiny=${pkgver}")
url="http://search.cpan.org/dist/Module-Build-Tiny"
source=("http://search.cpan.org/CPAN/authors/id/L/LE/LEONT/${_pkgname}-${pkgver}.tar.gz")
sha512sums=('7f0d01354eaa08611b6b207ef362fbebd941838c1191c652c014f3ac2fe0eee32c64f8eb6711ca557f4f021f6fab8f64e155adf7bf183952021e6af3da1533dc')

build() {
  ( export PERL_MM_USE_DEFAULT=1 PERL5LIB=""                 \
      PERL_AUTOINSTALL=--skipdeps                            \
      PERL_MM_OPT="INSTALLDIRS=vendor DESTDIR='$pkgdir'"     \
      PERL_MB_OPT="--installdirs vendor --destdir '$pkgdir'" \
      MODULEBUILDRC=/dev/null

    cd "${srcdir}/${_pkgname}-${pkgver}"
    /usr/bin/perl Build.PL
    ./Build
  )
}

check() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  ( export PERL_MM_USE_DEFAULT=1 PERL5LIB=""
    ./Build test
  )
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  ( export PERL_AUTOINSTALL=--skipdeps                       \
      PERL_MM_OPT="INSTALLDIRS=vendor DESTDIR='$pkgdir'"     \
      PERL_MB_OPT="--installdirs vendor --destdir '$pkgdir'"
    ./Build install
  )
  find "$pkgdir" -name .packlist -o -name perllocal.pod -delete
}

# Local Variables:
# mode: shell-script
# sh-basic-offset: 2
# End:
# vim:set ts=2 sw=2 et:
