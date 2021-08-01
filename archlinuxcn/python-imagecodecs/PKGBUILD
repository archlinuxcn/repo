# Maintainer: Butui Hu <hot123tea123@gmail.com>

_name=imagecodecs
pkgname=python-imagecodecs
pkgver=2021.7.30
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
  libaec
  libdeflate
  libavif
  libjpeg
  libjpeg-xl
  libmng
  libpng
  libtiff
  libwebp
  openjpeg2
  python-imread
  python-numpy
  snappy
  zfp
  zopfli
)
makedepends=(
  cython
  python-setuptools
)
source=("${_name}-${pkgver}.tar.gz::https://github.com/cgohlke/imagecodecs/archive/v${pkgver}.tar.gz")
sha256sums=('c3f10514ab14ba81f906d3e4f4b04f75208c7b48eb810d939a47fcc0581f027b')

build() {
  cd "${srcdir}/${_name}-${pkgver}"
  python setup.py build
}

package() {
  cd "${srcdir}/${_name}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:ts=2:sw=2:et:
