# Maintainer: hexchian <i at hexchain dot org>

pkgname=crun
pkgver=0.10.2
pkgrel=1
pkgdesc="A fast and lightweight fully featured OCI runtime and C library for running containers"
url="https://github.com/containers/crun"
license=('GPL3')
arch=('x86_64')
depends=('yajl' 'systemd-libs' 'libcap' 'libseccomp')
makedepends=('libtool' 'python3' 'go-md2man')
source=("https://github.com/containers/crun/releases/download/$pkgver/crun-$pkgver.tar.xz")
sha256sums=('3ebc10943e3384428c637b5c137ca1c7c15f129260ac55b2b74a4d0ba2887ef3')

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
