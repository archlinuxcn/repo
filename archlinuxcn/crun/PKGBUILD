# Maintainer: hexchian <i at hexchain dot org>

pkgname=crun
pkgver=0.10.6
pkgrel=1
pkgdesc="A fast and lightweight fully featured OCI runtime and C library for running containers"
url="https://github.com/containers/crun"
license=('GPL3')
arch=('x86_64')
depends=('yajl' 'systemd-libs' 'libcap' 'libseccomp')
makedepends=('libtool' 'python3' 'go-md2man')
source=("https://github.com/containers/crun/releases/download/$pkgver/crun-$pkgver.tar.xz")
sha256sums=('bd69ff6a4a3c9d8d2869100dcbbf074735ab9b854756a33560f4e3bd37bfecf1')

build() {
    cd "$srcdir/$pkgname-$pkgver"
    ./autogen.sh
    ./configure --prefix=/usr
    make
}

package() {
    cd "$srcdir/$pkgname-$pkgver"
    make DESTDIR="$pkgdir" install
}
