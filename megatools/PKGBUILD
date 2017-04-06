# Maintainer: Ondrej Jirman <megous@megous.com>

pkgname=megatools
pkgver=1.9.98
pkgrel=2
pkgdesc="Command line client application for Mega.nz"
arch=('i686' 'x86_64' 'armv7h')
url="http://megatools.megous.com"
license=('GPL')
depends=('curl' 'glib2')
makedepends=('asciidoc')
source=("http://megatools.megous.com/builds/megatools-${pkgver}.tar.gz")
options=(!libtool)
sha256sums=('9b0521a4d27dbc417fc8e12610ac1e1da729bf6d6eb5bef927ef3670b372a16f')

build() {
  cd "megatools-${pkgver}"

  ./configure --prefix=/usr

  make
}

package() {
  cd "megatools-${pkgver}"

  make install DESTDIR="${pkgdir}"
}
