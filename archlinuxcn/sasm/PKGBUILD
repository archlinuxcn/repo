# Maintainer:  twa022 <twa022 at gmail dot com>
# Contributor: Light2Yellow <alexvilchansky@yahoo.com>
# Contributor: yaroslav <proninyaroslav@mail.ru>
# Contributor: V0K3 <v0k3@inventati.org>

pkgname=sasm
pkgver=3.14.0
pkgrel=1
pkgdesc="Simple crossplatform IDE for NASM, GAS, FASM assembly languages"
arch=('i686' 'x86_64')
url="http://dman95.github.io/SASM/english.html"
license=('GPL3')
depends=('qt5-base' 'nasm' 'gdb' 'gcc' 'fasm')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/Dman95/SASM/archive/v${pkgver}.tar.gz")
sha256sums=('6c087bda9a7dfc7da2b8342c57c36f56fd2fa37414dfc2ab0da6aef28f97fc3d')

build() {
    cd "${pkgname^^}-${pkgver}"
    qmake PREFIX=/usr
    make
}

package() {
    cd "${pkgname^^}-${pkgver}"
    make INSTALL_ROOT="${pkgdir}" install
    # Don't provide fasm in the package, require it instead
    rm "${pkgdir}"/usr/bin/fasm
}
