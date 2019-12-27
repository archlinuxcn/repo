# Maintainer: hexchian <i at hexchain dot org>

pkgname=crun
pkgver=0.11
pkgrel=1
pkgdesc="A fast and lightweight fully featured OCI runtime and C library for running containers"
url="https://github.com/containers/crun"
license=('GPL3')
arch=('x86_64')
depends=('yajl' 'systemd-libs' 'libcap' 'libseccomp')
makedepends=('libtool' 'python3' 'go-md2man')
source=("https://github.com/containers/crun/releases/download/$pkgver/crun-$pkgver.tar.xz")
sha256sums=('cc1d3b459eb78d7c006372f2e197a81a0d549c8438c15edd6013be228ccd8fd8')

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
