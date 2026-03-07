# Maintainer: Butui Hu <hot123tea123@gmail.com>

_name=imagecodecs
pkgname=python-imagecodecs
pkgver=2026.3.6
pkgrel=1
pkgdesc='Image transformation, compression, and decompression codecs'
arch=('x86_64')
url='https://github.com/cgohlke/imagecodecs'
license=('BSD-3-Clause')
depends=(
  blosc
  blosc2
  brotli
  brunsli
  bzip2
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
  python-pillow
  snappy
  xz
  zfp
  zlib
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
)
sha256sums=('16e3449de17269523a01e0166bfe3e006d0af6c8b4b75c52adba773f1ba538f8')

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
