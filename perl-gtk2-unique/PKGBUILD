# Maintainer: Brian Bidulock <bidulock@openss7.org>
# Contributor: Crotok <crotok [at] mailbox [dot] org>
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Brian Bidulock <bidulock@openss7.org>
# Contributor: Michael Kogan <michael dot kogan at gmx dot net>

pkgname=perl-gtk2-unique
_cpanname=Gtk2-Unique
pkgver=0.05
pkgrel=22
pkgdesc="Perl bindings for the C library libunique"
arch=('i686' 'x86_64')
url="https://metacpan.org/release/${_cpanname}"
license=('LGPL' 'PerlArtistic')
makedepends=('perl-extutils-depends' 'perl-extutils-pkgconfig')
depends=('perl' 'gtk2-perl' 'libunique')
checkdepends=('xorg-server-xvfb')
options=('!emptydirs')
source=("http://search.cpan.org/CPAN/authors/id/P/PO/POTYL/${_cpanname}-${pkgver}.tar.gz"
        "$pkgname.patch"
		"fix_segfault_2nd_instance.patch")
md5sums=('0beb552933b765a017588563a71af123'
         'f8e15e1b93e2629e1745f8e4de8524ff'
         'b509a893e15c614dc668348c89e83c2d')

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