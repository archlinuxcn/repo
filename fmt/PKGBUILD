# Maintainer: Mihai Bişog <mihai.bisog at [gmail] d0t com>
pkgname=fmt
pkgver=4.0.0
pkgrel=2
pkgdesc="Open-source formatting library for C++."
arch=("i686" "x86_64")
url="http://fmtlib.net"
license=("BSD")
makedepends=("cmake")

source=("https://github.com/fmtlib/fmt/archive/$pkgver.tar.gz"
        "0001-Fix-a-segfault-in-test-on-glibc-2.26-551.patch"
        "0002-Fix-a-segfault-in-test-on-glibc-2.26-551-take-2.patch")
md5sums=('c9be9a37bc85493d1116b0af59a25eba'
         '95021c5ed1673d65b1c4ac54f047cc87'
         '3d41d1083621f8252949412493f6a207')

prepare() {
    # Fixes an issue leading to a test segfaulting when run with glibc2.26
    cd "$pkgname-$pkgver"
    patch -p 1 -i ${srcdir}/0001-Fix-a-segfault-in-test-on-glibc-2.26-551.patch
    patch -p 1 -i ${srcdir}/0002-Fix-a-segfault-in-test-on-glibc-2.26-551-take-2.patch
}

build() {
    cd "$pkgname-$pkgver"
    mkdir -p build && cd build

    cmake -DCMAKE_BUILD_TYPE=Release  \
          -DCMAKE_INSTALL_PREFIX=/usr \
          -DFMT_DOC=OFF               \
          ..
    make
}

check() {
    cd "$pkgname-$pkgver/build"
    make test
}

package() {
    cd "$pkgname-$pkgver/build"
    make DESTDIR="$pkgdir" install
    install -D -m644 ../LICENSE.rst "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    install -D -m644 ../ChangeLog.rst "${pkgdir}/usr/share/doc/${pkgname}/ChangeLog.rst"
}
