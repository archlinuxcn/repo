# Maintainer: Karol "Kenji Takahashi" Woźniak <kenji.sx>

pkgname=copyq
_realname=CopyQ
pkgver=3.0.3
pkgrel=1
pkgdesc="Clipboard manager with searchable and editable history."
url="https://github.com/hluk/CopyQ"
depends=('libxtst' 'qt5-script' 'hicolor-icon-theme')
optdepends=('copyq-plugin-itemweb')
makedepends=('cmake' 'qt5-tools' 'qt5-svg')
license=('GPL3')
arch=('i686' 'x86_64')
source=("https://github.com/hluk/${_realname}/archive/v${pkgver}.tar.gz")
md5sums=('54a0157d5a0d234b6afd798ed01f4c7f')

build() {
    mkdir "${srcdir}/build"
    cd "${srcdir}/build"
    cmake \
        -DWITH_WEBKIT=0 \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DWITH_QT5=TRUE \
        "${srcdir}/${_realname}-${pkgver}"
    make
}

package() {
    cd "${srcdir}/build"
    make DESTDIR="${pkgdir}" install
}

# vim:set ts=4 sw=4 et:
