# Maintainer: Joffrey <j-off@live.fr>
# Contributor: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: localizator <localizator@ukr.net>
# Contributor: Edvinas Valatka <edacval@gmail.com>

pkgname=seafile-client
pkgver=7.0.5
pkgrel=1
pkgdesc='GUI client for synchronizing your local files with seafile server'
arch=('i686' 'x86_64' 'armv7h' 'armv6h' 'aarch64')
url="https://github.com/haiwen/$pkgname"
license=('Apache')
depends=(
    'seafile'
    'qt5-base'
    'qt5-webengine'
    'qt5-webkit'
    'qt5-tools'
    'gtk-update-icon-cache'
)
makedepends=("cmake")
conflicts=('seafile-client-qt5')
provides=('seafile-client-qt5')
source=("$pkgname-v$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('7e86cb3e055f5cf5a51c287a5d494cad5dcd9d7d6c355dbfe1f512eccaa97e9e')

prepare() {
  cd "$srcdir"
  rm -rf build
  mkdir -p build
}

build() {
  cd "$srcdir/build"
  cmake \
    -DBUILD_SHIBBOLETH_SUPPORT=ON \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX='/usr' \
    "$srcdir/$pkgname-$pkgver"
  make
}

package () {
  cd "$srcdir/build"
  make DESTDIR="$pkgdir" install
}
