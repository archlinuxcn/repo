# Maintainer: Kolei Chen <chenkolei at gmail dot com>

pkgname=xosview2
pkgver=2.3.1
pkgrel=1
pkgdesc="A lightweight system monitor"
url="http://xosview.sourceforge.net/"
license=('GPL' 'BSD')
arch=('x86_64' 'armv7h' 'aarch64')
depends=('gawk' 'libxext' 'libxft' 'libxpm' 'libsm')
source=("https://downloads.sourceforge.net/project/xosview/xosview2-${pkgver}.tar.gz")
sha512sums=('c90fc4f79d1f776eba90620376d318302135fc18e79a49e1aa57607276b57d46c66eb647ad92b3ac314b74d64247887e81e1541f81dd276e1e5ef2206e241060')

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

