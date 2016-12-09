# Maintainer: SY.Zhang <lastavengers@archlinuxcn.org>
pkgname=loc
pkgver=0.3.4
pkgrel=1
pkgdesc='Count lines of code quickly'
arch=('x86_64' 'i386')
url='https://github.com/cgag/loc'
license=('MIT')
makedepends=('cargo')
source=("https://github.com/cgag/${pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('01fd16f0f82e016da95c5ad66a0390372ca1bf1ded9981a7a1f004e4a50bb804')

build () {
    cd ${pkgname}-${pkgver}
    cargo update
    cargo build --release
}

package () {
    cd ${pkgname}-${pkgver}/target/release
    install -Dm755 ${pkgname} ${pkgdir}/usr/bin/${pkgname}
}
