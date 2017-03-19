# Maintainer: Zanny <lordzanny@gmail.com>
# Contributor: Ivan Shapovalov <intelfx@intelfx.name>

pkgname=clinfo
pkgver=2.1.17.02.09
pkgrel=1
pkgdesc="Print all known information about all available OpenCL platforms and devices in the system"
arch=(i686 x86_64)
url="https://github.com/Oblomov/clinfo"
license=('custom:Public Domain')
depends=(opencl-icd-loader)
makedepends=(opencl-headers)
source=("https://github.com/Oblomov/clinfo/archive/$pkgver.tar.gz")
md5sums=('2ef6d1d958f138817ce89e4bddd49f10')

build() {
    cd $srcdir/$pkgname-$pkgver
    make
}

package() {
    cd $srcdir/$pkgname-$pkgver
    install -D -m755 clinfo "$pkgdir/usr/bin/clinfo"
    install -D -m644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -D -m644 man/clinfo.1 "$pkgdir/usr/share/man/man1/clinfo.1"
}
