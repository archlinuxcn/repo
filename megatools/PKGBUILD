# Maintainer: Ondrej Jirman <megous@megous.com>

pkgname=megatools
pkgver=1.10.2
pkgrel=1
pkgdesc="Command line client application for Mega.nz"
arch=('i686' 'x86_64' 'armv7h')
url="http://megatools.megous.com"
license=('GPL')
depends=('curl' 'glib2' 'openssl')
makedepends=('asciidoc')
source=("http://megatools.megous.com/builds/megatools-${pkgver}.tar.gz")
options=(!libtool)
sha256sums=('179e84c68e24696c171238a72bcfe5e28198e4c4e9f9043704f36e5c0b17c38a')

build() {
  cd "megatools-${pkgver}"

  ./configure --prefix=/usr

  make
}

package() {
  cd "megatools-${pkgver}"

  make install DESTDIR="${pkgdir}"
}
