# Maintainer: Jonathan Steel <jsteel at aur.archlinux.org>
# Contributor: Justin Davis <jrcd83@gmail.com>

pkgname=perl-mouse
pkgver=2.3.0
pkgrel=1
pkgdesc="Moose minus the antlers"
arch=('i686' 'x86_64')
url="http://search.cpan.org/dist/Mouse"
license=('PerlArtistic' 'GPL')
depends=('perl')
makedepends=('perl-test-exception' 'perl-test-fatal' 'perl-module-build'
             'perl-module-build-xsutil' 'perl-test-requires'
             'perl-test-leaktrace' 'perl-test-output' 'perl-test-deep'
             'perl-io-string')
source=(http://search.cpan.org/CPAN/authors/id/G/GF/GFUJI/Mouse-$pkgver.tar.gz)
md5sums=('aae2b55f280f773a92fa16c6bdcc358d')

build() {
  cd "$srcdir"/Mouse-$pkgver

  ( export PERL_MM_USE_DEFAULT=1 PERL5LIB=""                  \
      PERL_AUTOINSTALL=--skipdeps                             \
      PERL_MM_OPT="INSTALLDIRS=vendor DESTDIR='$pkgdir'"      \
      PERL_MB_OPT="--installdirs vendor --destdir '$pkgdir'"  \
      MODULEBUILDRC=/dev/null

    /usr/bin/perl Build.PL
    ./Build
  )
}

check() {
  cd "$srcdir"/Mouse-$pkgver

  ( export PERL_MM_USE_DEFAULT=1 PERL5LIB=""
    ./Build test
  )
}

package() {
  cd "$srcdir"/Mouse-$pkgver

  ./Build install
}
