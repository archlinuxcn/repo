# Contributor: Laurent Tréguier <laurent@treguier.org>

pkgname=libui
pkgver=0.4.alpha
_pkgver=alpha4
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
md5sums=('9ca3e7e387eaaa9bf8c71f0c64b9a271')

build() {
    cd "${srcdir}/${pkgname}-${_pkgver}"
    mkdir build
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
