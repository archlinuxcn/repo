# Maintainer: Steven Allen <steven@stebalien.com>
# Contributor: trile7 at gmail dot com
# Contributor: Ernia <monghitri@aruba.it>

pkgname=yad
pkgver=0.36.2
pkgrel=1
pkgdesc="A fork of zenity - display graphical dialogs from shell scripts or command line"
url="http://sourceforge.net/projects/yad-dialog"
arch=('x86_64' 'i686')
license=('GPL3')
depends=('gtk3' 'webkitgtk')
makedepends=('intltool')
source=("${url}/files/${pkgname}-${pkgver}.tar.xz")
sha256sums=('70675218c03ec14ebad090c465cb4e86b30ae2907a53def02dd8228f8182040e')


prepare() {
  cd "${srcdir}/${pkgname}-${pkgver}"
}

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  ./configure --prefix=/usr --with-gtk=gtk3 --enable-icon-browser --enable-html
  make
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}" install

}

