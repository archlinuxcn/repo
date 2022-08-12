# Maintainer: Jesse Lentz <jesse@twosheds.org>

pkgname=iwgtk
pkgver=0.8
pkgrel=2
pkgdesc='Lightweight wireless network management GUI (front-end for iwd)'
arch=(x86_64)
url='https://github.com/J-Lentz/iwgtk'
license=(GPL3)
depends=('iwd>=1.28' 'gtk4>=4.6' qrencode adwaita-icon-theme)
makedepends=('meson>=0.60.0' scdoc)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/J-Lentz/iwgtk/archive/v0.8.tar.gz")
sha256sums=(38e81e67004bbd246b6551ffc812b6ab019f84a7329f134bb8031eb61d9d732c)

build() {
    cd ${pkgname}-${pkgver}
    meson setup --prefix /usr build
    cd build
    meson compile
}

package() {
    cd ${pkgname}-${pkgver}/build
    meson install --destdir ${pkgdir}
}
