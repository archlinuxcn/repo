# Maintainer: Butui Hu <hot123tea123@gmail.com>

_name=imagecodecs
pkgname=python-imagecodecs
pkgver=2023.9.4
pkgrel=1
pkgdesc='Image transformation, compression, and decompression codecs'
arch=('x86_64')
url='https://github.com/cgohlke/imagecodecs'
license=('BSD')
depends=(
  blosc
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
  libjxl
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
sha256sums=('b8b4e1b1691123aa9b5e8e4686a0805e1215eae3da5949697b7fc925ad2e90e0'
            '4bc2af7f9d7894c71fdb9507af30a633db83901b85a24838c4d1a09c6bedb606')

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
