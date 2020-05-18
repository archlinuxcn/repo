# Maintainer: Ondrej Jirman <megous@megous.com>

pkgname=megatools
pkgver=1.11.0.git.20200404
_pkgver=1.11.0-git-20200404
pkgrel=1
pkgdesc="Command line client application for Mega.nz"
arch=('i686' 'x86_64' 'armv7h')
url="http://megatools.megous.com"
license=('GPL')
depends=('curl' 'glib2' 'openssl')
makedepends=(asciidoc meson)
source=("https://megatools.megous.com/builds/experimental/megatools-${_pkgver}.tar.gz")
sha256sums=('999404dd065ecadbc117311e4de431d85eca98a2c4bfd3f29a4c30372e213b9c')

build() {
  meson --prefix /usr --buildtype=plain megatools-${_pkgver} build -Dsymlinks=true
  ninja -C build
}

package() {
  DESTDIR="$pkgdir" ninja -C build install
}

