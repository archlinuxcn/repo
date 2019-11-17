# Maintainer: peeweep <peeweep at 0x0 dot ee>
# Contributor: Anatol Pomozov <anatol@google.com>

pkgname=muduo
pkgver=2.0.0
pkgrel=5
pkgdesc='A C++ non-blocking multi-threaded network library'
url='https://github.com/chenshuo/muduo'
license=(BSD)
arch=(i686 x86_64)
depends=(protobuf)
makedepends=(cmake boost)
options=(staticlibs)
source=(${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha256sums=('bf7ae8bd9fd54567c93e12ddbfbc25a69fe6a50e625f02743e7268df3760dc13')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  sed -i '/-Werror/d' CMakeLists.txt
  sed -i 's/option(MUDUO_BUILD_EXAMPLES "Build Muduo examples" ON/option(MUDUO_BUILD_EXAMPLES "Build Muduo examples" OFF/' CMakeLists.txt
  INSTALL_DIR=/usr ./build.sh
}

package() {
  cd "${srcdir}/build/release-cpp11"
  make install DESTDIR="${pkgdir}"
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}/License" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
