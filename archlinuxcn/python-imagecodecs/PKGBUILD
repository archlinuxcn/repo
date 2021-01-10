# Maintainer: Butui Hu <hot123tea123@gmail.com>

_name=imagecodecs
pkgname=python-imagecodecs
pkgver=2021.1.8
pkgrel=2
pkgdesc='Image transformation, compression, and decompression codecs'
arch=('x86_64')
url='https://github.com/cgohlke/imagecodecs'
license=('BSD')
depends=(
  blosc
  brotli
  brunsli
  charls
  jxrlib
  lcms2
  libaec
  libdeflate
  libavif
  libjpeg
  libmng
  libpng
  libtiff
  libwebp
  openjpeg2
  python-imread
  python-numpy
  snappy
  zfp
)
makedepends=(python-setuptools cython)
source=("${_name}-${pkgver}.tar.gz::https://github.com/cgohlke/imagecodecs/archive/v${pkgver}.tar.gz")
sha256sums=('0f705fa8a471c794228eb08d868dc807c5b6211400af6404e9cd21ad0a01dd7e')

prepare() {
  sed -i "s,/usr/include/openjpeg-2.3,/usr/include/openjpeg-2.4," "${srcdir}/${_name}-${pkgver}/setup.py"
}

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
