# Maintainer:  Caleb Maclennan <caleb@alerque.com>
# Contributor: Jordi De Groof <jordi.degroof@gmail.com>
# Contributor: Andre Klitzing <aklitzing@gmail.com>

pkgname=lcov
pkgver=1.15
pkgrel=2
pkgdesc="front-end for GCC's coverage testing tool gcov"
arch=('any')
url="https://github.com/linux-test-project/$pkgname"
license=('GPL')
depends=('perl')
backup=(etc/lcovrc)
source=("https://github.com/linux-test-project/$pkgname/releases/download/v$pkgver/$pkgname-$pkgver.tar.gz"
        "handle-equals-signs.patch"
        "fix-undef-behaviour.patch")
sha256sums=('c1cda2fa33bec9aa2c2c73c87226cfe97de0831887176b45ee523c5e30f8053a'
            '54728aa4e244d3662c65ba91fb486dc1d5c64d9d55745ee334c4131109dc233c'
            'ceaf41f7cc9cea5a6fc4b0385ffef10d1ab8812acd2a5b16dcd8d7bca7120488')

prepare () {
    cd "$pkgname-$pkgver"
    patch -p1 -i "$srcdir"/handle-equals-signs.patch
    patch -p1 -i "$srcdir"/fix-undef-behaviour.patch
}

package () {
    cd "$pkgname-$pkgver"
    make PREFIX="/usr" CFG_DIR=/etc DESTDIR="$pkgdir" install
}
