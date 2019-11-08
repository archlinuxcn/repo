# Maintainer: hexchian <i at hexchain dot org>

pkgname=crun
pkgver=0.10.4
pkgrel=1
pkgdesc="A fast and lightweight fully featured OCI runtime and C library for running containers"
url="https://github.com/containers/crun"
license=('GPL3')
arch=('x86_64')
depends=('yajl' 'systemd-libs' 'libcap' 'libseccomp')
makedepends=('libtool' 'python3' 'go-md2man')
source=("https://github.com/containers/crun/releases/download/$pkgver/crun-$pkgver.tar.xz")
sha256sums=('21f2eeb6a71ec6ff35e214c8f27429199f4eb4b71ef7a77a7792157cce257df6')

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
