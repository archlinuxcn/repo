# Maintainer: taotieren <admin@taotieren.com>

pkgname=notepad---git
pkgver=2.11.r4.g1045cfe
pkgrel=2
pkgdesc="Notepad-- 是使用C++编写的轻量级文本编辑器, 简称ndd, 可以支持Window/Mac/Linux操作系统平台。"
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
source=("${pkgname}::git+${url}.git")
sha256sums=('SKIP')

pkgver() {
    cd "${srcdir}/${pkgname}/"
    git describe --long --tags | sed 's/^v//g;s/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
    cd "${srcdir}/${pkgname}"

    cp -rv how_build/* .
    sed -i 's/\bintptr_t\b/__intptr_t/g' src/qscint/src/xmlMatchedTagsHighlighter.cpp
    sed -i 's/\bintptr_t\b/__intptr_t/g' src/qscint/src/xmlMatchedTagsHighlighter.h
    sed -i 's/NotePad--/notepad--/g' CMakeLists.txt
    sed -i '7s/NotePad--/notepad--/' src/linux/usr/share/applications/NotePad--.desktop


    cmake -D CMAKE_BUILD_TYPE=None \
        -D CMAKE_INSTALL_PREFIX=/usr \
        -B build \
        -G Ninja \
        -W no-dev

    ninja -C build
}

package() {
    DESTDIR="${pkgdir}" ninja -C "${srcdir}"/${pkgname}/build install
}
