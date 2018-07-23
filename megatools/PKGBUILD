# Maintainer: Ondrej Jirman <megous@megous.com>

pkgname=megatools
pkgver=1.10.0
pkgrel=1
pkgdesc="Command line client application for Mega.nz"
arch=('i686' 'x86_64' 'armv7h')
url="http://megatools.megous.com"
license=('GPL')
depends=('curl' 'glib2' 'openssl')
makedepends=('asciidoc')
source=("http://megatools.megous.com/builds/megatools-${pkgver}.tar.gz")
options=(!libtool)
sha256sums=('788a51d0977db95c371c97917aee3d39e145044b6bb70d671bc76c2ea6c4171b')

build() {
  cd "megatools-${pkgver}"

  ./configure --prefix=/usr

  make
}

package() {
  cd "megatools-${pkgver}"

  make install DESTDIR="${pkgdir}"
}
