# Maintainer: Amin Vakil <info AT aminvakil DOT com>
# Contributor: Lamelos <lamelos at gmail.com>

pkgname=butane
pkgver=0.23.0
pkgrel=1
pkgdesc="Human readable Butane Configs into machine readable Ignition Configs Translator"
arch=("any")
url="https://github.com/coreos/butane"
license=("Apache")
makedepends=("git" "go" "make")
source=("git+${url}.git#tag=v${pkgver}"
        "change-bin-dir.patch")
sha256sums=('73c1b8ad824ad78e4428aef381b85c4152dada3f50b9857ae4882630d44dc726'
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
