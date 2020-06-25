# Maintainer: Brian Bidulock <bidulock@openss7.org>
# Contributor: Crotok <crotok [at] mailbox [dot] org>
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Brian Bidulock <bidulock@openss7.org>
# Contributor: Michael Kogan <michael dot kogan at gmx dot net>

pkgname=perl-gtk2-unique
_cpanname=Gtk2-Unique
pkgver=0.05
pkgrel=26
pkgdesc="Perl bindings for the C library libunique"
arch=('i686' 'x86_64')
url="https://metacpan.org/release/${_cpanname}"
license=('LGPL' 'PerlArtistic')
makedepends=('perl-extutils-depends' 'perl-extutils-pkgconfig')
depends=('perl' 'gtk2-perl' 'libunique')
checkdepends=('xorg-server-xvfb')
options=('!emptydirs')
source=("https://cpan.metacpan.org/authors/id/P/PO/POTYL/${_cpanname}-${pkgver}.tar.gz"
        "$pkgname.patch"
		"fix_segfault_2nd_instance.patch")
md5sums=('0beb552933b765a017588563a71af123'
         'f8e15e1b93e2629e1745f8e4de8524ff'
         'b509a893e15c614dc668348c89e83c2d')
sha512sums=('9ed700de45e6d7e5410ff4b4313869be9127b7933faf862f4f34f4330165dbda4b1d983efddedcd71487d0cdbf10982a7b76af7cf60339ae3359f57271177492'
            '9893a480f60a28eb50c053fbd840eec514cddb3bca322fe5ebdbc74b9382514cb5dc2d1c2a3fa740d42f2129b683adb9d99090ab5c99ae42c6eff3fb3da379ff'
            '594097e881c30178c3084a026d9a3a0cd2eb86e5bdd89faf19e29ee5c911a184af1f33b3b1b0b1ae693b354b6ffd754c7b43c3783b19f3ec6c545b90e3dcfe0e')

build() {
  cd  $_cpanname-$pkgver
  patch -Np1 -i ../$pkgname.patch
  patch -Np1 -i ../fix_segfault_2nd_instance.patch
  PERL_MM_USE_DEFAULT=1 perl Makefile.PL INSTALLDIRS=vendor
  sed -e 's,q(build/doc.pl),q(./build/doc.pl),g' -i Makefile
  make
}

check() {
  cd  $_cpanname-$pkgver
  xvfb-run -a -s "-extension GLX -screen 0 1280x1024x24" make test
}

_perl_depends() {
# template start; name=perl-binary-module-dependency; version=1;
if [[ $(find "$pkgdir/usr/lib/perl5/" -name "*.so") ]]; then
	_perlver_min=$(perl -e '$v = $^V->{version}; print $v->[0].".".($v->[1]);')
	_perlver_max=$(perl -e '$v = $^V->{version}; print $v->[0].".".($v->[1]+1);')
	depends+=("perl>=$_perlver_min" "perl<$_perlver_max")
fi
# template end;
}

package() {
  cd  $_cpanname-$pkgver
  make install DESTDIR="$pkgdir"
  find "$pkgdir" -name '.packlist' -delete
  find "$pkgdir" -name '*.pod' -delete
  _perl_depends
}
