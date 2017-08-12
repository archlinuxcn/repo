# $Id: PKGBUILD 174746 2016-05-11 04:30:34Z fyan $
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: TDY <tdy@archlinux.info>
# Contributor: Olaf Leidinger <leidola@newcon.de>
# Maintainer: zoe <chp321 [at] gmail [dot] com>

pkgname=perl-gtk2-imageview
pkgver=0.05
pkgrel=10
pkgdesc="Perl bindings to the GtkImageView image viewer widget"
arch=('i686' 'x86_64')
url="http://search.cpan.org/dist/Gtk2-ImageView/"
license=('LGPL3')
depends=('perl' 'cairo-perl' 'glib-perl' 'gtk2-perl' 'gtkimageview')
makedepends=('perl-extutils-depends' 'perl-extutils-pkgconfig')
checkdepends=('perl-test-pod' 'xorg-server-xvfb')
options=('!emptydirs')
source=("http://search.cpan.org/CPAN/authors/id/R/RA/RATCLIFFE/Gtk2-ImageView-$pkgver.tar.gz")
md5sums=('7c961071b347b6a64b8351fdd87ec4c0')

build() {
  cd "$srcdir/Gtk2-ImageView-$pkgver"
  PERL_MM_USE_DEFAULT=1 perl Makefile.PL INSTALLDIRS=vendor
  PERL_USE_UNSAFE_INC=1 make
}

check() {
  cd "$srcdir/Gtk2-ImageView-$pkgver"
  xvfb-run -a -s "-extension GLX -screen 0 1280x1024x24" make test
}

package() {
  cd "$srcdir/Gtk2-ImageView-$pkgver"
  make DESTDIR="$pkgdir" install
# template start; name=perl-binary-module-dependency; version=1;
#if [[ $(find "$pkgdir/usr/lib/perl5/" -name "*.so") ]]; then
#	_perlver_min=$(perl -e '$v = $^V->{version}; print $v->[0].".".($v->[1]);')
#	_perlver_max=$(perl -e '$v = $^V->{version}; print $v->[0].".".($v->[1]+1);')
#	depends+=("perl>=$_perlver_min" "perl<$_perlver_max")
#fi
# template end;
}
