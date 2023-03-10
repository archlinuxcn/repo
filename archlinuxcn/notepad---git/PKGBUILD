# Maintainer: taotieren <admin@taotieren.com>

pkgname=notepad---git
pkgver=1.23.r113.g12b1a07
pkgrel=1
pkgdesc="Notepad-- 是一个简单的国产跨平台文本编辑器，是替换 Notepad++ 的一种选择。其内置强大的代码对比功能，让你丢掉付费的 Beyond Compare。"
arch=('x86_64')
url="https://gitee.com/cxasm/notepad--"
license=('GPL3')
provides=(${pkgname%-git} notepadplugin)
conflicts=(${pkgname%-git})
_qt=qt5
depends=($_qt-base
        $_qt-xmlpatterns
        qscintilla-$_qt)
makedepends=(cmake
            ninja
            git
            $_qt-tools)
source=("${pkgname}::git+${url}.git#branch=cmake-dev")
sha256sums=('SKIP')

pkgver() {
    cd "${srcdir}/${pkgname}/"
    git describe --long --tags | sed 's/v//g;s/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
    cd "${srcdir}/${pkgname}/"

    cmake -S . \
        -D USE_LINUX_UNIVERSAL=ON \
        -D CMAKE_BUILD_TYPE=None \
        -D CMAKE_INSTALL_PREFIX=/usr \
        -B build \
        -G Ninja \
        -W no-dev

    ninja -C build
}

package() {
    DESTDIR="${pkgdir}" ninja -C "${srcdir}"/${pkgname}/build install
}
