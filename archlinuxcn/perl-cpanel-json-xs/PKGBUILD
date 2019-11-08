# Contributor: ordoban <dirk.langer@vvovgonik.de>
# Generator  : CPANPLUS::Dist::Arch 1.32

pkgname='perl-cpanel-json-xs'
_pkgname='Cpanel-JSON-XS'
pkgver='4.17'
pkgrel='2'
pkgdesc="cPanel fork of JSON::XS, fast and correct serializing"
arch=('i686' 'x86_64')
license=('PerlArtistic' 'GPL')
options=('!emptydirs')
depends=('perl>=0')
makedepends=()
url="https://metacpan.org/release/$_pkgname"
source=("https://cpan.metacpan.org/authors/id/R/RU/RURBAN/$_pkgname-$pkgver.tar.gz")
md5sums=('baa45d9fc27df7cd11adecc42a85bc04')
sha512sums=('1e827af8d51f4bf984e8c016bc34e66d7b3364556a8295a1e6a4bcd17e959a8c56fb7873d7c3884ab740eb85203c3aecd09349b14a297ca8ba5cd995815fabf1')
_distdir="$_pkgname-$pkgver"

build() {
  export PERL_MM_USE_DEFAULT=1 PERL5LIB=""                      \
         PERL_AUTOINSTALL=--skipdeps                            \
         PERL_MM_OPT="INSTALLDIRS=vendor DESTDIR='$pkgdir'"     \
         PERL_MB_OPT="--installdirs vendor --destdir '$pkgdir'" \
         MODULEBUILDRC=/dev/null

  cd "$srcdir/$_distdir"
  /usr/bin/perl Makefile.PL
  make
}

check() {
  cd "$srcdir/$_distdir"
  export PERL_MM_USE_DEFAULT=1 PERL5LIB="."
  make test
}

package() {
  cd "$srcdir/$_distdir"
  make install

  find "$pkgdir" \( -name .packlist -o -name perllocal.pod \) -delete
}

# Local Variables:
# mode: shell-script
# sh-basic-offset: 2
# End:
# vim:set ts=2 sw=2 et:
