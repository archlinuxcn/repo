# Maintainer: hexchain <i at hexchain.org>

pkgname=range-v3
pkgver=0.3.0
pkgrel=1
pkgdesc="Experimental range library for C++11/14/17"
arch=('any')
url='https://github.com/ericniebler/range-v3'
license=('custom')
makedepends=('git')
source=("git+https://github.com/ericniebler/range-v3.git#tag=${pkgver}")
md5sums=('SKIP')

package() {
    mkdir -p "$pkgdir/usr/include"
    cp -rv --no-preserve=ownership "$srcdir/range-v3/include/"* "$pkgdir/usr/include"
    # install custom license
    install -Dm644 "$srcdir/range-v3/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
