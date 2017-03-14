# Maintainer: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: localizator <localizator@ukr.net>
# Contributor: Edvinas Valatka <edacval@gmail.com>

pkgname=seafile-client
pkgver=6.0.3
pkgrel=1
pkgdesc="GUI client for synchronizing your local files with seafile server"
arch=('i686' 'x86_64')
url="https://github.com/haiwen/${pkgname}"
license=('Apache')
depends=('ccnet' "seafile" "qt5-tools" "qt5-webkit" "qt5-base"
         "gtk-update-icon-cache" "qt5-webengine")
makedepends=("cmake")
conflicts=('seafile-client-qt5')
provides=('seafile-client-qt5')
source=("${pkgname}-v${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('4de4d8f9633af28c1421d38180d3f33f78fcfd3b7cb0e8d82d1ede7515aa8992')

prepare() {
  cd "${srcdir}"

  rm -rf build
  mkdir -p build
}

build () {
  cd "$srcdir/build"

  cmake \
    -DBUILD_SHIBBOLETH_SUPPORT=ON \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    "${srcdir}/${pkgname}-${pkgver}"

  make
}

package () {
  cd "${srcdir}/build"

  make DESTDIR="${pkgdir}" install
}
