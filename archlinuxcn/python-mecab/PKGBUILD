# Maintainer: nosada <ngsksdt@gmail.com>

pkgname=python-mecab
_pkgname=mecab-python
pkgver=0.996
pkgrel=2
pkgdesc="Morphological Analysis Tool - Python3 interface"
arch=('x86_64' 'i686')
url="http://taku910.github.io/mecab/"
license=('BSD' 'LGPL2.1' 'GPL2')
depends=("python" "mecab")
source=("${_pkgname}-${pkgver}.tar.gz::https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7UlJpaWJKM01KRVE"
        "setup.patch")
sha1sums=('b7801d78b4def5118903f3d7b97968b106aa8ea8'
          'd9a39080d9f742821ac1da41c510ca8db53b0201')

prepare(){
  cd ${srcdir}/${_pkgname}-${pkgver}
  patch < ${srcdir}/setup.patch
}

build() {
  cd ${srcdir}/${_pkgname}-${pkgver}
  python setup.py build_ext
}

package() {
  cd ${srcdir}/${_pkgname}-${pkgver}

  python setup.py install --root=${pkgdir}
  install -Dm644 COPYING \
            ${pkgdir}/usr/share/licenses/${pkgname}/COPYING
}

# vim:set ts=2 sw=2 et:
