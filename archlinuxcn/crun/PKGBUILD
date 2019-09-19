# Maintainer: hexchian <i at hexchain dot org>

pkgname=crun
pkgver=0.9.1
pkgrel=1
pkgdesc="A fast and lightweight fully featured OCI runtime and C library for running containers"
url="https://github.com/containers/crun"
license=('GPL3')
arch=('x86_64')
depends=('yajl' 'systemd-libs' 'libcap' 'libseccomp')
makedepends=('libtool' 'python3' 'go-md2man')
source=("https://github.com/containers/crun/releases/download/$pkgver/crun-$pkgver.tar.xz")
sha256sums=('a6884a14d57a441dd86c07912b5ba734b634d805922a4916085c5f4379237d8a')

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
