# Maintainer: Shengyu Zhang <la@archlinuxcn.org>
pkgname=loc
pkgver=0.4.1
pkgrel=2
pkgdesc='Count lines of code quickly'
arch=('x86_64' 'i386')
url='https://github.com/cgag/loc'
license=('MIT')
makedepends=('cargo')
source=("https://github.com/cgag/${pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('1e8403fd9a3832007f28fb389593cd6a572f719cd95d85619e7bbcf3dbea18e5')

build () {
    cd ${pkgname}-${pkgver}
    cargo update
    cargo build --release
}

package () {
    cd ${pkgname}-${pkgver}/target/release
    install -Dm755 ${pkgname} ${pkgdir}/usr/bin/${pkgname}
}
