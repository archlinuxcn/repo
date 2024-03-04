# Maintainer: Butui Hu <hot123tea123@gmail.com>

_name=imagecodecs
pkgname=python-imagecodecs
pkgver=2024.1.1
pkgrel=3
pkgdesc='Image transformation, compression, and decompression codecs'
arch=('x86_64')
url='https://github.com/cgohlke/imagecodecs'
license=('BSD-3-Clause')
depends=(
  blosc
  blosc2
  brotli
  brunsli
  charls
  giflib
  glibc
  jxrlib
  lcms2
  lerc
  libaec
  libavif
  libdeflate
  libheif
  libjpeg-turbo
  libjxl
  libpng
  libtiff
  libwebp
  lz4
  lzfse
  openjpeg2
  python-numpy
  snappy
  xz
  zfp
  zlib-ng
  zopfli
  zstd
)
makedepends=(
  cython
  python-build
  python-installer
  python-setuptools
  python-wheel
)
source=("${_name}-${pkgver}.tar.gz::https://github.com/cgohlke/imagecodecs/archive/v${pkgver}.tar.gz"
        "0001-fix-extension-deps.patch"
)
sha256sums=('6af69181a3fe828f9fea5fd440af1b88610fd05665665e6885c3a84c1055b648'
            'f4086c9d7541bc7e9925ebadfe3313addd971da42bdc33ca84e41c9f47e323d2')

prepare() {
  cd "${_name}-${pkgver}"
  patch -p1 -i "${srcdir}/0001-fix-extension-deps.patch"
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
