# $Id: PKGBUILD 174744 2016-05-11 04:23:20Z fyan $
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Shanto <shanto@hotmail.com>
# Contributor: TDY <tdy@gmx.com>
# Maintainer: zoe <chp321 [at] gmail [dot] com>

pkgname=perl-goo-canvas
pkgver=0.06
pkgrel=10
pkgdesc="Perl bindings for GooCanvas"
arch=('i686' 'x86_64')
url="http://search.cpan.org/dist/Goo-Canvas/"
license=('GPL' 'PerlArtistic')
depends=('perl' 'cairo-perl' 'glib-perl' 'goocanvas1' 'gtk2-perl')
makedepends=('perl-extutils-depends' 'perl-extutils-pkgconfig')
options=('!emptydirs')
source=("http://search.cpan.org/CPAN/authors/id/Y/YE/YEWENBIN/Goo-Canvas-$pkgver.tar.gz")
md5sums=('7dfe0be8c17bfd641d18384d4fd8fb23')

build() {
  cd "$srcdir/Goo-Canvas-$pkgver"
  PERL_MM_USE_DEFAULT=1 perl Makefile.PL INSTALLDIRS=vendor
  PERL_USE_UNSAFE_INC=1 make
}

check() {
  cd "$srcdir/Goo-Canvas-$pkgver"
  make test
}

package() {
  cd "$srcdir/Goo-Canvas-$pkgver"
  make install DESTDIR="$pkgdir"
# template start; name=perl-binary-module-dependency; version=1;
#if [[ $(find "$pkgdir/usr/lib/perl5/" -name "*.so") ]]; then
#	_perlver_min=$(perl -e '$v = $^V->{version}; print $v->[0].".".($v->[1]);')
#	_perlver_max=$(perl -e '$v = $^V->{version}; print $v->[0].".".($v->[1]+1);')
#	depends+=("perl>=$_perlver_min" "perl<$_perlver_max")
#fi
# template end;
}
