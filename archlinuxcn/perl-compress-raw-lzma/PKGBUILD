# Maintainer : Xeonacid <h.dwwwwww@gmail.com>
# Maintainer : Leon Möller <jkhsjdhjs at totally dot rip>
# Contributor: Asger Hautop Drewsen <asgerdrewsen@gmail.com>

pkgname='perl-compress-raw-lzma'
pkgver=2.213
pkgrel=1
pkgdesc="Low-Level Perl Interface to lzma compression library"
_dist=Compress-Raw-Lzma
arch=('i686' 'x86_64')
url="https://metacpan.org/release/$_dist"
license=('GPL-1.0-or-later' 'Artistic-1.0-Perl')
options=('!emptydirs' 'purge')
depends=('glibc' 'perl' 'perl-pod-markdown' 'xz')
source=("https://cpan.metacpan.org/authors/id/P/PM/PMQS/$_dist-$pkgver.tar.gz")
md5sums=('f3bb656d9524b1d8ac4a47707dcd1f1d')
sha512sums=('7e41eaaf8a244a2e2e06f8c7b23bd88d7afd83daf44022d03f650c3990a7ffe5d39bb153fe4583711fd860e7e8e6eb19b7397fcb93d56b6df3c7f95bcdb5ad75')

build() {
  cd $_dist-$pkgver
  unset PERL5LIB PERL_MM_OPT PERL_LOCAL_LIB_ROOT
  export PERL_MM_USE_DEFAULT=1 PERL_AUTOINSTALL=--skipdeps
  /usr/bin/perl Makefile.PL
  make
}

check() {
  cd $_dist-$pkgver
  unset PERL5LIB PERL_MM_OPT PERL_LOCAL_LIB_ROOT
  export PERL_MM_USE_DEFAULT=1
  make test
}

package() {
  cd $_dist-$pkgver
  unset PERL5LIB PERL_MM_OPT PERL_LOCAL_LIB_ROOT
  make install INSTALLDIRS=vendor DESTDIR="$pkgdir"
}

# Local Variables:
# mode: shell-script
# sh-basic-offset: 2
# End:
# vim:set ts=2 sw=2 et:
