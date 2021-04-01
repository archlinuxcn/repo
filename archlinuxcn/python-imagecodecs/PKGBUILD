# Maintainer: Butui Hu <hot123tea123@gmail.com>

_name=imagecodecs
pkgname=python-imagecodecs
pkgver=2021.3.31
pkgrel=1
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
  zopfli
)
makedepends=(python-setuptools cython)
source=("${_name}-${pkgver}.tar.gz::https://github.com/cgohlke/imagecodecs/archive/v${pkgver}.tar.gz")
sha256sums=('9bd5cb7e6490d96eddd2d8c225a1b160384ec2b583e713437be9e30174ffa170')

prepare() {
  sed -i "s/del EXTENSIONS\['zopfli'\]/pass/" ${srcdir}/${_name}-${pkgver}/setup.py
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
