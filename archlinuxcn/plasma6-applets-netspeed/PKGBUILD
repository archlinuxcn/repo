# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
pkgname=plasma6-applets-netspeed
_pkgname=plasma-applet-netspeed-widget
pkgver=3.1
pkgrel=1
pkgdesc="Plasma 6 widget that displays the currently used network bandwidth"
arch=('any')
url="https://github.com/dfaust/plasma-applet-netspeed-widget"
license=('GPL-2.0-only')
conflicts=('plasma5-applets-netspeed')
replaces=('plasma5-applets-netspeed')
depends=(
    'awk'
    'plasma-workspace'
)
makedepends=(
    'cmake'
    'extra-cmake-modules'
)
optdepends=('kdeplasma-addons: support to launch a user defined application when the applet is clicked')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/dfaust/plasma-applet-netspeed-widget/archive/refs/tags/v${pkgver}.tar.gz")
b2sums=('1f54130cb59b355be2b240d3e01d0b9abea9fd76f8843c190098e15bb630092742ce604c8567fd8952069e165d0ac2853dcf0203fc022de7b54ac3dc1229e8ca')

build() {
    cmake -B build -S ${_pkgname}-${pkgver} \
        -DCMAKE_BUILD_TYPE='None' \
        -DCMAKE_INSTALL_PREFIX='/usr' \
        -Wno-dev
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
}

