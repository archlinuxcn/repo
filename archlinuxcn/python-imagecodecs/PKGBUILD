# Maintainer: Butui Hu <hot123tea123@gmail.com>

_name=imagecodecs
pkgname=python-imagecodecs
pkgver=2026.11.11
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
  openjph
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
  pkgconf
  python-build
  python-installer
  python-setuptools
  python-wheel
)
source=("${_name}-${pkgver}.tar.gz::https://github.com/cgohlke/imagecodecs/archive/v${pkgver}.tar.gz"
)
sha256sums=('c6eac78c57aa1952bf4e73fd4927c162e863e0e7b6f3675e61adbd0e59a90bb2')

build() {
  cd "${srcdir}/${_name}-${pkgver}"
  # jxrlib installs its headers under /usr/include/libjxr/* (subdirectories),
  # but setup.py hardcodes the old flat /usr/include/jxrlib path. Feed the
  # correct include flags from its pkg-config file (distutils honors CPPFLAGS).
  export CPPFLAGS="${CPPFLAGS} $(pkg-config --cflags libjxr)"
  python -m build --wheel --no-isolation --skip-dependency-check
}

package() {
  cd "${srcdir}/${_name}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:ts=2:sw=2:et:
