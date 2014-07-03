# CPAN Name  : Net-OAuth
# Contributor: Anonymous
# Generator  : CPANPLUS::Dist::Arch 1.28

pkgname='perl-net-oauth'
pkgver='0.28'
pkgrel='4'
pkgdesc="An implementation of the OAuth protocol"
arch=('any')
license=('PerlArtistic' 'GPL')
options=('!emptydirs')
depends=('perl-class-accessor>=0.31' 'perl-class-data-inheritable>=0.06' 'perl-digest-hmac' 'perl-digest-sha1>=2.12' 'perl-uri' 'perl-libwww' 'perl-file-slurp-tiny')
makedepends=()
checkdepends=('perl-test-warn>=0.21')
url='http://search.cpan.org/dist/Net-OAuth'
source=('http://search.cpan.org/CPAN/authors/id/K/KG/KGRENNAN/Net-OAuth-0.28.tar.gz')
md5sums=('336d7fb22e945f014e1bce0f49fcfad9')
sha512sums=('b38c3784221bdf56b5b55021cc7e74cf6c5ce47b6743b6fefae9e148ff61d3c1e068aa5829dfed13ffd070e1286ab0d743e2f7b7c900f5fd8cf78f788cff70c4')

build() {
  cd "$srcdir/Net-OAuth-0.28"
  PERL_MM_USE_DEFAULT=1 perl Makefile.PL INSTALLDIRS=vendor
  make
}

check() {
  cd "$srcdir/Net-OAuth-0.28"
  PERL_MM_USE_DEFAULT=1
  make test
}

package() {
  cd "$srcdir/Net-OAuth-0.28"
  make install DESTDIR="$pkgdir"
  find "$pkgdir" -name '.packlist' -o -name '*.pod' -delete
}
