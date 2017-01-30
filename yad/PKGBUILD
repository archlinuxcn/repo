# Maintainer: Aaron Fischer <mail@aaron-fischer.net>
# Contributor: Steven Allen <steven@stebalien.com>
# Contributor: trile7 at gmail dot com
# Contributor: Ernia <monghitri@aruba.it>

pkgname=yad
pkgver=0.38.1
pkgrel=2
pkgdesc="A fork of zenity - display graphical dialogs from shell scripts or command line"
url="http://sourceforge.net/projects/yad-dialog"
arch=('x86_64' 'i686')
license=('GPL3')
depends=('gtk3' 'webkit2gtk')
makedepends=('intltool')
source=("${url}/files/${pkgname}-${pkgver}.tar.xz")
sha256sums=('a17ba052a11f0ca6209131c766b5ec171e5e1c63f37ce648349a627152186790')

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

