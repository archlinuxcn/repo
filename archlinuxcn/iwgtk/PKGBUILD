# Maintainer: Jesse Lentz <jesse@twosheds.org>

pkgname=iwgtk
pkgver=0.9
pkgrel=1
pkgdesc='Lightweight wireless networking GUI (front-end for iwd)'
arch=(x86_64)
url='https://github.com/J-Lentz/iwgtk'
license=(GPL3)
depends=('iwd>=1.29' 'gtk4>=4.6' qrencode adwaita-icon-theme)
makedepends=('meson>=0.60.0' scdoc)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/J-Lentz/iwgtk/archive/v0.9.tar.gz")
sha256sums=(84a82dc730fe536034a65d148840e975c1353f4114db527439170ff410583d31)

build() {
    cd ${pkgname}-${pkgver}
    meson setup --prefix /usr --buildtype release --warnlevel 0 build
    cd build
    meson compile
}

package() {
    cd ${pkgname}-${pkgver}/build
    meson install --destdir ${pkgdir}
}
