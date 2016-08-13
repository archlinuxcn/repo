# Maintainer: Steven Allen <steven@stebalien.com>
# Contributor: trile7 at gmail dot com
# Contributor: Ernia <monghitri@aruba.it>

pkgname=yad
pkgver=0.37.0
pkgrel=1
pkgdesc="A fork of zenity - display graphical dialogs from shell scripts or command line"
url="http://sourceforge.net/projects/yad-dialog"
arch=('x86_64' 'i686')
license=('GPL3')
depends=('gtk3' 'webkitgtk')
makedepends=('intltool')
source=("${url}/files/${pkgname}-${pkgver}.tar.xz")
sha256sums=('91efaf24b56dfbed8e86e4af800f13ec9cca4b550b82b65552aaab40ebd3183a')


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

