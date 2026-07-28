# Maintainer: Max Gautier <mg@max.gautier.name>
pkgname=xdg-terminal-exec
pkgver=0.14.2
pkgrel=1
pkgdesc="Proposed standard to launching desktop apps with Terminal=true"
arch=(any)
url="https://gitlab.freedesktop.org/Vladimir-csp/$pkgname"
makedepends=('scdoc')
checkdepends=('bats')
license=('GPL-3.0-or-later')
source=("${pkgname}-${pkgver}::$url/-/archive/v${pkgver}/${pkgname}-v${pkgver}.tar.gz")
sha256sums=('0919e2257224bd43079de28b0140602b587fd9f37ec29935c98ca8792bb51c44')
b2sums=('d2d08603168955c8735f57a2649a365333944a87068594c94c83673fe51492ee7f06e838f8f2a18f4dbfc05a772b295c2d00cb11fa38a7436179dba6f2487bd6')

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
