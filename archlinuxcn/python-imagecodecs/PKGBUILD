# Maintainer: Butui Hu <hot123tea123@gmail.com>

_name=imagecodecs
pkgname=python-imagecodecs
pkgver=2020.5.30
pkgrel=2
pkgdesc='Image transformation, compression, and decompression codecs'
arch=('x86_64')
url='https://github.com/cgohlke/imagecodecs'
license=('BSD')
depends=(
  blosc
  brotli
  charls
  jxrlib
  lcms2
  libaec
  libjpeg
  libmng
  libpng
  libtiff
  libwebp
  openjpeg2
  python-numpy
  snappy
  zfp
  zopfli
)
makedepends=(python-setuptools cython)
source=("${_name}-${pkgver}.tar.gz::https://github.com/cgohlke/imagecodecs/archive/v${pkgver}.tar.gz"
    '0001-fix-setup.patch::https://github.com/hubutui/imagecodecs/commit/e5ae4f1458b7a33dbaefb1b6b75c44d14b0fa79a.patch'
    )
sha256sums=('4d750b4eb6b2bb33ae14897d6d5affe8ae22f5a6e8a04823f19bb1a05619a4b4'
            'a2eeb124a594f1a2d2f0303c4a51758a713fd84bd9ab6b16841c72e95f74b828')

prepare() {
  cd "${srcdir}/${_name}-${pkgver}"
  patch -p1 -i "${srcdir}/0001-fix-setup.patch"
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
