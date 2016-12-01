# Maintainer: SY.Zhang <lastavengers@archlinuxcn.org>
pkgname=loc
pkgver=0.3.2
pkgrel=3
pkgdesc='Count lines of code quickly'
arch=('x86_64' 'i386')
url='https://github.com/cgag/loc'
license=('MIT')
makedepends=('cargo')
source=("https://github.com/cgag/${pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('0b805d53326f269e8fe21f709dc69947820fda1f291040e9225f93aef614daea')

build () {
    cd ${pkgname}-${pkgver}
    cargo update
    cargo build --release
}

package () {
    cd ${pkgname}-${pkgver}/target/release
    install -Dm755 ${pkgname} ${pkgdir}/usr/bin/${pkgname}
}
