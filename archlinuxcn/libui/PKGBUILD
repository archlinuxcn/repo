# Contributor: Laurent Tréguier <laurent@treguier.org>

pkgname=libui
pkgver=0.4.1.alpha
_pkgver=alpha4.1
pkgrel=1
pkgdesc='A portable GUI library for C'
arch=('i686' 'x86_64')
url='https://github.com/andlabs/libui'
license=('MIT')
depends=('gtk3' 'libx11' 'libxcb' 'libffi')
makedepends=('cmake')
provides=('libui')
conflicts=('libui-git')
source=("https://github.com/andlabs/libui/archive/${_pkgver}.tar.gz")
md5sums=('8c6263ee0a91f76412bffdd104c2be73')

build() {
    cd "${srcdir}/${pkgname}-${_pkgver}"
    mkdir -p build
    cd build
    cmake ..
    make
}

package() {
    cd "${srcdir}/${pkgname}-${_pkgver}"
    install -d "${pkgdir}/usr/"{include,lib}
    install -Dm644 ui.h "${pkgdir}/usr/include"
    install -Dm644 ui_unix.h "${pkgdir}/usr/include"
    install -Dm755 build/out/libui.so.0 "${pkgdir}/usr/lib"
    install -Dm755 build/out/libui.so "${pkgdir}/usr/lib"
}
