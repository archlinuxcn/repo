# Maintainer: Aaron Fischer <mail@aaron-fischer.net>
# Contributor: Steven Allen <steven@stebalien.com>
# Contributor: trile7 at gmail dot com
# Contributor: Ernia <monghitri@aruba.it>

pkgname=yad
pkgver=0.42.0
pkgrel=1
pkgdesc="A fork of zenity - display graphical dialogs from shell scripts or command line"
url="https://github.com/v1cont/yad"
arch=('x86_64' 'i686')
license=('GPL3')
depends=('gtk3' 'webkit2gtk')
makedepends=('autoconf' 'automake' 'intltool')
source=("${url}/archive/v${pkgver}.tar.gz")
sha512sums=('700b11f449b63ec1bc8fecf0d2df3ed18bc7078472de0f3ee034c28e3e096eb61559529cc094c76fc8a9959bbb3e5f159d621ad9739d857b0d9b8d7ff386deaa')

build() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    autoreconf -ivf
    intltoolize
    ./configure \
      --prefix=/usr \
      --with-gtk=gtk3 \
      --enable-icon-browser \
      --enable-html \
      --enable-gio \
      --enable-spell \
      --enable-sourceview

    make
}

package() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    make DESTDIR="${pkgdir}" install
}

