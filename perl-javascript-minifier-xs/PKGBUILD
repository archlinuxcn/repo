# Contributor: John D Jones III AKA jnbek <jnbek1972 -_AT_- g m a i l -_Dot_- com>
# Generator  : CPANPLUS::Dist::Arch 1.32

pkgname='perl-javascript-minifier-xs'
pkgver='0.11'
pkgrel='1'
pkgdesc="XS based JavaScript minifier"
arch=('i686' 'x86_64')
license=('PerlArtistic' 'GPL')
options=('!emptydirs')
depends=('perl')
makedepends=()
url='https://metacpan.org/release/JavaScript-Minifier-XS'
source=('http://search.cpan.org/CPAN/authors/id/G/GT/GTERMARS/JavaScript-Minifier-XS-0.11.tar.gz')
md5sums=('bd8544287ecd1b651367295485f4a5b0')
sha512sums=('736294c898d7806eae509b0d0c14cfcbb783ac335fe6c08bed9c00a52643b3e6d0ade124735d7de8d2203bf404448889e0e84b3097e316d0ef444f1603cbbdef')
_distdir="JavaScript-Minifier-XS-0.11"

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
