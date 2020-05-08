# Maintainer: Konstantin Shalygin <k0ste@k0ste.ru>
# Contributor: Konstantin Shalygin <k0ste@k0ste.ru>

pkgname='libyang'
pkgver='1.0.167'
pkgrel='1'
pkgdesc='A YANG data modelling language parser and toolkit written (and providing API) in C.'
url="https://github.com/CESNET/${pkgname}"
arch=('x86_64')
license=('BSD')
depends=('pcre')
makedepends=('cmake' 'swig')
checkdepends=('cmocka')
conflicts=('libyang-git' 'libyang-devel-git')
source=("${url}/archive/v${pkgver}.tar.gz")
sha256sums=('2431fa5c7cfbe6a6f2c0873547b976f018438967adfe268726911dd3d95eaa31')

prepare() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  mkdir build
}

build() {
  cd "${srcdir}/${pkgname}-${pkgver}/build"
  cmake .. \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=lib \
    -DCMAKE_BUILD_TYPE=Release \
    -DENABLE_LYD_PRIV=ON \
    -DENABLE_BUILD_TESTS=ON \
    -DGEN_LANGUAGE_BINDINGS=ON \
    -DGEN_PYTHON_BINDINGS=OFF \
    -DGEN_CPP_BINDINGS=ON
  make
}

check() {
  cd "${srcdir}/${pkgname}-${pkgver}/build"
  make test
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}/build"
  make DESTDIR="${pkgdir}" install
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
