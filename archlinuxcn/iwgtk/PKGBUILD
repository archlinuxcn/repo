# Maintainer: Jesse Lentz <jesse@twosheds.org>

pkgname=iwgtk
pkgver=0.5
pkgrel=1
pkgdesc='Lightweight, graphical wifi management front-end for iwd'
arch=(x86_64)
url='https://github.com/J-Lentz/iwgtk'
license=(GPL3)
depends=('iwd>=1.28' gtk4 adwaita-icon-theme)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/J-Lentz/iwgtk/archive/v0.5.tar.gz")
sha256sums=(5465721f79090d342c389c8748ba6ef679fa83ae5ed23cea90bcb4e1b9017689)

build() {
    cd ${pkgname}-${pkgver}
    make
}

package() {
    cd ${pkgname}-${pkgver}
    make PREFIX=/usr DESTDIR=${pkgdir} install
}
