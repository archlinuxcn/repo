# Maintainer: Jesse Lentz <jesselnz@gmail.com>

pkgname=iwgtk
pkgver=0.4
pkgrel=1
pkgdesc='Lightweight, graphical wifi management utility'
arch=(x86_64)
url='https://github.com/J-Lentz/iwgtk'
license=(GPL3)
depends=(iwd gtk3)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/J-Lentz/iwgtk/archive/v0.4.tar.gz")
sha256sums=(71bb85546a55bf710052d4947f6be5f5a01033d04d2d14a85a7e734dd570657d)

build() {
    cd ${pkgname}-${pkgver}
    make
}

package() {
    cd ${pkgname}-${pkgver}
    make prefix=/usr DESTDIR=${pkgdir} install
}
