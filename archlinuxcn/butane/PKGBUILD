# Maintainer: Amin Vakil <info AT aminvakil DOT com>
# Contributor: Lamelos <lamelos at gmail.com>

pkgname=butane
pkgver=0.24.0
pkgrel=1
pkgdesc="Human readable Butane Configs into machine readable Ignition Configs Translator"
arch=("any")
url="https://github.com/coreos/butane"
license=("Apache")
makedepends=("git" "go" "make")
source=("git+${url}.git#tag=v${pkgver}"
        "change-bin-dir.patch")
sha256sums=('be358d91918f52f5f28bbf602d7dd02e0daab08ad5696a184256b93ccea0fe7c'
            'bdb99494bf163a89269858f2aeb28b389837e9eb0b92b7b2c20e5a03f4941cde')

prepare() {
    cd "${srcdir}"
    patch --forward --strip=1 --input="${srcdir}/change-bin-dir.patch"
}

build() {
    cd "${srcdir}/${pkgname}"
    ./build
}

package() {
    cd "${srcdir}/${pkgname}"
    install -D -m 755 "bin/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"
}
