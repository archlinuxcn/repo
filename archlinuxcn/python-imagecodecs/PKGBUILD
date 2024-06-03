# Maintainer: Butui Hu <hot123tea123@gmail.com>

_name=imagecodecs
pkgname=python-imagecodecs
pkgver=2024.6.1
pkgrel=2
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
        "0001-fix-extension-deps.patch"
)
sha256sums=('71b321db0dd9849a38e9c4d2f2eb1e32ca1eaead1e67da564bfd3a1470a359b3'
            '125276c6fd91ddcb49b0646c5c07515d43f033fa7da66899229a31dc4fa6c3e1')

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
