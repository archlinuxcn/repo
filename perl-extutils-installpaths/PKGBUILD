# Contributor: xRemaLx <anton.komolov@gmail.com>

pkgname='perl-extutils-installpaths'
_pkgname='ExtUtils-InstallPaths'
pkgver=0.010
pkgrel=1
pkgdesc="ExtUtils::InstallPaths - Build.PL install path logic made easy"
arch=(any)
license=('perl')
url="http://search.cpan.org/dist/ExtUtils-InstallPaths/"
options=(!emptydirs)

depends=('perl>=5.10.1' 'perl-extutils-config>=0.002')
makedepends=('perl')

provides=("extutils-installpaths=${pkgver}" "ExtUtils::InstallPaths=${pkgver}" "perl-extutils-installpaths=${pkgver}")

source=("http://search.cpan.org/CPAN/authors/id/L/LE/LEONT/${_pkgname}-${pkgver}.tar.gz")
sha512sums=('3639e8e05b2d59d1a5c4548d74e51158ce6e6b2260d2958f5500b7bb2f64470b72b8b9690e3ec917ff6db8baf0a81038178336bccbc272116e16b520cac73f0f')

build() {
  ( export PERL_MM_USE_DEFAULT=1 PERL5LIB=""                 \
      PERL_AUTOINSTALL=--skipdeps                            \
      PERL_MM_OPT="INSTALLDIRS=vendor DESTDIR='$pkgdir'"     \
      PERL_MB_OPT="--installdirs vendor --destdir '$pkgdir'" \
      MODULEBUILDRC=/dev/null

    cd "${srcdir}/${_pkgname}-${pkgver}"
    /usr/bin/perl Makefile.PL
    make
  )
}

check() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  ( export PERL_MM_USE_DEFAULT=1 PERL5LIB=""
    make test
  )
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  make install
  find "$pkgdir" -name .packlist -o -name perllocal.pod -delete
}

# vim:set ts=2 sw=2 et:
