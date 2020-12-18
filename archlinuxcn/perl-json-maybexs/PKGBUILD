# Maintainer : <michael dot kogan at gmx dot net>
# Contributor: John D Jones III AKA jnbek <jnbek1972 -_AT_- g m a i l -_Dot_- com>
# Generator  : CPANPLUS::Dist::Arch 1.32

pkgname='perl-json-maybexs'
pkgver='1.004003'
pkgrel='1'
pkgdesc="Use Cpanel::JSON::XS with a fallback to JSON::XS and JSON::PP"
arch=('any')
license=('PerlArtistic' 'GPL')
options=('!emptydirs')
depends=('perl>=5.006')
makedepends=('perl-test-needs')
optdepends=('perl-cpanel-json-xs: Using Cpanel-JSON-XS')
url='https://metacpan.org/release/JSON-MaybeXS'
source=("https://cpan.metacpan.org/authors/id/E/ET/ETHER/JSON-MaybeXS-$pkgver.tar.gz")
md5sums=('e46181e34588428d317932744597a7ab')
_distdir="JSON-MaybeXS-$pkgver"

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