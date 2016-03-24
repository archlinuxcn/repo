# Maintainer: Steven Allen <steven@stebalien.com>
# Contributor: trile7 at gmail dot com
# Contributor: Ernia <monghitri@aruba.it>

pkgname=yad
pkgver=0.35.0
pkgrel=1
pkgdesc="A fork of zenity - display graphical dialogs from shell scripts or command line"
url="http://sourceforge.net/projects/yad-dialog"
arch=('x86_64' 'i686')
license=('GPL3')
depends=('gtk3' 'webkitgtk')
makedepends=('intltool')
install='yad.install'
source=($url/files/${pkgname}-${pkgver}.tar.xz)
sha256sums=('cd98bdbd888e6e3b7d91bd6ddd2f6c3a61c4b0a64b2f96081c63893468e43ba0')

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

