# Maintainer: Butui Hu <hot123tea123@gmail.com>

_name=imagecodecs
pkgname=python-imagecodecs
pkgver=2024.1.1
pkgrel=1
pkgdesc='Image transformation, compression, and decompression codecs'
arch=('x86_64')
url='https://github.com/cgohlke/imagecodecs'
license=('BSD')
depends=(
  blosc
  blosc2
  brotli
  brunsli
  cfitsio
  charls
  jxrlib
  lcms2
  lerc
  libaec
  libavif
  libdeflate
  libheif
  libjpeg-turbo
  # libjxl
  libmng
  libpng
  libtiff
  libwebp
  lzfse
  openjpeg2
  python-imread
  python-numpy
  snappy
  zfp
  zlib-ng
  zopfli
)
makedepends=(
  cython
  python-build
  python-installer
  python-setuptools
  python-wheel
)
source=("${_name}-${pkgver}.tar.gz::https://github.com/cgohlke/imagecodecs/archive/v${pkgver}.tar.gz"
        "0001.fix-deps.patch"
)
sha256sums=('6af69181a3fe828f9fea5fd440af1b88610fd05665665e6885c3a84c1055b648'
            'bac18e10bc97a92b2d805fcfe4796a02bb81b746d25b984bf2502fc3cb7c80c4')

prepare() {
  cd "${_name}-${pkgver}"
  patch -p1 -i "${srcdir}/0001.fix-deps.patch"
}

build() {
  cd "${srcdir}/${_name}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${srcdir}/${_name}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:ts=2:sw=2:et:
