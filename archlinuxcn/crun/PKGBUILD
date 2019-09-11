# Maintainer: hexchian <i at hexchain dot org>

pkgname=crun
pkgver=0.8
pkgrel=2
pkgdesc="A fast and lightweight fully featured OCI runtime and C library for running containers"
url="https://github.com/containers/crun"
license=('GPL3')
arch=('x86_64')
depends=('yajl' 'systemd-libs' 'libcap' 'libseccomp')
makedepends=('libtool' 'python3' 'go-md2man')
source=("https://github.com/containers/crun/releases/download/0.8/crun-0.8.tar.xz")
sha256sums=('9f4798fcf70420d0634b3eb44eb7747add60d8f5771f6805cb152a197a42c30a')

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
