# Maintainer: Jesse Lentz <jesse@twosheds.org>

pkgname=iwgtk
pkgver=0.7
pkgrel=1
pkgdesc='Lightweight wireless network management GUI (front-end for iwd)'
arch=(x86_64)
url='https://github.com/J-Lentz/iwgtk'
license=(GPL3)
depends=('iwd>=1.28' 'gtk4>=4.6' qrencode adwaita-icon-theme)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/J-Lentz/iwgtk/archive/v0.7.tar.gz")
sha256sums=(ab33211e8e65e723bfe9ac3276dd2fcaec50a6fffe06c44d21615e612755e744)

build() {
    cd ${pkgname}-${pkgver}
    make
}

package() {
    cd ${pkgname}-${pkgver}
    make PREFIX=/usr DESTDIR=${pkgdir} install
}
