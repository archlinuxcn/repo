# Maintainer: Aaron Fischer <mail@aaron-fischer.net>
# Contributor: Steven Allen <steven@stebalien.com>
# Contributor: trile7 at gmail dot com
# Contributor: Ernia <monghitri@aruba.it>

pkgname=yad
pkgver=0.39.0
pkgrel=1
pkgdesc="A fork of zenity - display graphical dialogs from shell scripts or command line"
url="http://sourceforge.net/projects/yad-dialog"
arch=('x86_64' 'i686')
license=('GPL3')
depends=('gtk3' 'webkit2gtk')
makedepends=('intltool')
source=("${url}/files/${pkgname}-${pkgver}.tar.xz")
sha256sums=('11e114c1434f4fa42b2c9a7e6a5f818beead8a697a429906a59fb6f85723a9ed')

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

