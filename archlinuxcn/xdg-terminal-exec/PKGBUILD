# Maintainer: Max Gautier <mg@max.gautier.name>
pkgname=xdg-terminal-exec
pkgver=0.14.3
pkgrel=1
pkgdesc="Proposed standard to launching desktop apps with Terminal=true"
arch=(any)
url="https://gitlab.freedesktop.org/Vladimir-csp/$pkgname"
makedepends=('scdoc')
checkdepends=('bats')
license=('GPL-3.0-or-later')
source=("${pkgname}-${pkgver}::$url/-/archive/v${pkgver}/${pkgname}-v${pkgver}.tar.gz")
sha256sums=('bfa291f6ad70fc61abd0b45510b799cb24c1c11f0b5cdc7b7538169688f1df79')
b2sums=('3ca3f4996fdbb11e98dfd84aceae3ac576c1652497e8a97627065de9b92df6f4b508afd4667e0a64b26d94850acbdbd10014cd60f5969cb3178a19682ca4ff51')

check() {
    cd "$pkgname-v$pkgver"
    bats "test/"
}

build() {
    make -C "$pkgname-v$pkgver"
}

package() {
    make -C "$pkgname-v$pkgver" prefix="$pkgdir/usr" install
}
