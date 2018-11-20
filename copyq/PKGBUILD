# Maintainer: Batou <batou at cryptolab net>
# Contributor: Karol "Kenji Takahashi" Woźniak <kenji.sx>

pkgname=copyq
pkgver=3.7.1
pkgrel=1
pkgdesc="Clipboard manager with searchable and editable history"
url="https://github.com/hluk/${pkgname}"
depends=('libxtst' 'qt5-script' 'qt5-svg' 'qt5-x11extras')
optdepends=('copyq-plugin-itemweb')
makedepends=('cmake' 'qt5-tools')
license=('GPL3')
arch=('x86_64')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('927c2c2df919c2323a7bbc0f24025bb06e54ad6c4cbf5bbc8dcf86ac0f4f6fc7')

build() {
    cd "CopyQ-${pkgver}"
    cmake -DCMAKE_BUILD_TYPE=Release -DWITH_WEBKIT=0 -DCMAKE_INSTALL_PREFIX=/usr -DWITH_QT5=TRUE .
    make
}

package() {
    cd "CopyQ-${pkgver}"
    make DESTDIR="${pkgdir}" install
}
