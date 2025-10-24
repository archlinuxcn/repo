# Maintainer : Xeonacid <h.dwwwwww@gmail.com>
# Maintainer : Leon Möller <jkhsjdhjs at totally dot rip>
# Contributor: Asger Hautop Drewsen <asgerdrewsen@gmail.com>

pkgname='perl-compress-raw-lzma'
pkgver=2.214
pkgrel=1
pkgdesc="Low-Level Perl Interface to lzma compression library"
_dist=Compress-Raw-Lzma
arch=('i686' 'x86_64')
url="https://metacpan.org/release/$_dist"
license=('GPL-1.0-or-later' 'Artistic-1.0-Perl')
options=('!emptydirs' 'purge')
depends=('glibc' 'perl' 'perl-pod-markdown' 'xz')
source=("https://cpan.metacpan.org/authors/id/P/PM/PMQS/$_dist-$pkgver.tar.gz")
md5sums=('63ebaa251c380c4c296b47b4dc628ca1')
sha512sums=('27d6c2d5f060b6105121f556a19903aa280724873118badd58ac32eb2d87eef8a716d719fbb7db24f0ddcd5a6d68ba362641a9577ec86624951073cd2ce2ac25')

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
