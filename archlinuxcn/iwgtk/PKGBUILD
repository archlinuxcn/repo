# Maintainer: Jesse Lentz <jesse@twosheds.org>

pkgname=iwgtk
pkgver=0.6
pkgrel=1
pkgdesc='Lightweight wireless network management GUI (front-end for iwd)'
arch=(x86_64)
url='https://github.com/J-Lentz/iwgtk'
license=(GPL3)
depends=('iwd>=1.28' gtk4 adwaita-icon-theme)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/J-Lentz/iwgtk/archive/v0.6.tar.gz")
sha256sums=(43e128c1ef123d115cda34a66f9a79b63560e0e7b658a6f34c60ddeb3a740704)

build() {
    cd ${pkgname}-${pkgver}
    make
}

package() {
    cd ${pkgname}-${pkgver}
    make PREFIX=/usr DESTDIR=${pkgdir} install
}
