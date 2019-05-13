# Maintainer: Kolei Chen <chenkolei at gmail dot com>

pkgname=xosview2
pkgver=2.3.0
pkgrel=1
pkgdesc="A lightweight system monitor"
url="http://xosview.sourceforge.net/"
license=('GPL' 'BSD')
arch=('x86_64' 'armv7h' 'aarch64')
depends=('gawk' 'libxext' 'gcc' 'libxft' 'libxpm' 'libsm')
source=("https://downloads.sourceforge.net/project/xosview/xosview2-${pkgver}.tar.gz")
sha512sums=('75ea06dd0542773d465a3aa4cc617f28a537dcb7c2acf87b30ea0845a0a59dcd36127a8b167d7e23974bcd39f9a9338e1277fc8e440b18da921bc427b5ee616d')

prepare() {
cd $srcdir/$pkgname-$pkgver
./configure --prefix=/usr
}

build() {
cd $srcdir/$pkgname-$pkgver
make $MAKEFLAGS
}

package() {
cd $srcdir/$pkgname-$pkgver
make DESTDIR=$pkgdir install
}

