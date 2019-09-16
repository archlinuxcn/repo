# Maintainer: Aaron Fischer <mail@aaron-fischer.net>
# Contributor: Steven Allen <steven@stebalien.com>
# Contributor: trile7 at gmail dot com
# Contributor: Ernia <monghitri@aruba.it>

pkgname=yad
pkgver=4.1
pkgrel=1
pkgdesc="A fork of zenity - display graphical dialogs from shell scripts or command line"
url="https://github.com/v1cont/yad"
arch=('x86_64' 'i686')
license=('GPL3')
depends=('gtk3' 'webkit2gtk' 'gtkspell3')
makedepends=('autoconf' 'automake' 'intltool')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz")
sha512sums=('440218a26f6c8d6d33cc016204e5101d3fe967e4e0d029160c5fcca588543ed76cfb1e39be92eb067ac292d27e144e4253a0526b83608ee7717288c27dce2005')
build() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    autoreconf -ivf
    intltoolize
    LIBS="-lglib-2.0" ./configure \
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

