# Maintainer: Ariel AxionL <axionl@aosc.io>
# Contributor: Yuan Zhou <xyyqzy@hotmail.com>

pkgname=landrop-git
pkgver=r59.ee8144a
pkgrel=3
pkgdesc="Drop any files to any devices on your LAN."
arch=('x86_64')
url="https://github.com/LANDrop/LANDrop"
license=('BSD')
depends=('libsodium' 'qt5-base' 'hicolor-icon-theme')
makedepends=('git')
conflicts=('landrop')
provides=('landrop')
source=("${pkgname}::git+$url.git")
sha512sums=('SKIP')

pkgver() {
    cd "${srcdir}/${pkgname}"
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
    mkdir -p build
    cd build
    PREFIX=/usr qmake "${srcdir}/${pkgname}/LANDrop"
    make
}

package() {
    install -Dm644 "${srcdir}/${pkgname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

    cd build
    make "INSTALL_ROOT=${pkgdir}" install
}
# vim set: ts=4 sw=4 et
