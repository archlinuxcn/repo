# Maintainer: Kewl <xrjy@nygb.rh.bet(rot13)>
# Contributor: Karol "Kenji Takahashi" Woźniak <kenji.sx>

pkgname=copyq
pkgver=3.5.0
pkgrel=1
pkgdesc="Clipboard manager with searchable and editable history"
url="https://github.com/hluk/${pkgname}"
depends=('libxtst' 'qt5-script' 'qt5-svg' 'qt5-x11extras')
optdepends=('copyq-plugin-itemweb')
makedepends=('cmake' 'qt5-tools')
license=('GPL3')
arch=('x86_64')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('86876e9ca66d0ac57ce86512df73f36bae3f10f06a9c66d05dc8785abf884df6')

build() {
    cd "CopyQ-${pkgver}"
    cmake -DCMAKE_BUILD_TYPE=Release -DWITH_WEBKIT=0 -DCMAKE_INSTALL_PREFIX=/usr -DWITH_QT5=TRUE .
    make
}

package() {
    cd "CopyQ-${pkgver}"
    make DESTDIR="${pkgdir}" install
}
