# Maintainer: Peter Tirsek <peter@tirsek.com>

pkgname=perl-pod-markdown
pkgver=3.400
pkgrel=1
pkgdesc='Convert POD to Markdown'
_dist=Pod-Markdown
arch=('any')
url="https://metacpan.org/release/$_dist"
license=('GPL' 'PerlArtistic')
depends=('perl>=5.8.0' 'perl-uri')
checkdepends=('perl-test-differences')
optdepends=('perl-html-parser: for nicer encoding of HTML entities')
options=('!emptydirs')
source=("http://www.cpan.org/authors/id/R/RW/RWSTAUNER/${_dist}-${pkgver}.tar.gz")
sha256sums=("a626e99bcd4e7d214e43d4722a54e3aafac3713862f7479cfb94a0e2879f8442")

build() {
  cd "$srcdir/$_dist-$pkgver"
  unset PERL5LIB PERL_MM_OPT PERL_LOCAL_LIB_ROOT
  export PERL_MM_USE_DEFAULT=1 PERL_AUTOINSTALL=--skipdeps
  /usr/bin/perl Makefile.PL
  make
}

check() {
  cd "$srcdir/$_dist-$pkgver"
  unset PERL5LIB PERL_MM_OPT PERL_LOCAL_LIB_ROOT
  export PERL_MM_USE_DEFAULT=1
  make test
}

package() {
  cd "$srcdir/$_dist-$pkgver"
  unset PERL5LIB PERL_MM_OPT PERL_LOCAL_LIB_ROOT
  make install INSTALLDIRS=vendor DESTDIR="$pkgdir"
}
