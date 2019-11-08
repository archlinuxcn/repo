# Maintainer: pingplug < aur at pingplug dot me >

pkgbase=python-openslide
pkgname=('python-openslide' 'python2-openslide')
pkgver=1.1.1
pkgrel=2
pkgdesc="A simple interface to read whole-slide images in Python"
arch=('any')
url="http://openslide.org"
license=('LGPL')
makedepends=('python-setuptools'
             'python2-setuptools')
source=("https://github.com/openslide/openslide-python/releases/download/v${pkgver}/openslide-python-${pkgver}.tar.xz")
sha256sums=('e3c1f27e4704221327d3c74b0960742079b18fea2d1896eda71a3efdd3f9d3f7')

prepare() {
  cd "${srcdir}"
  cp -a "openslide-python-${pkgver}"{,-py2}
}

build() {
  cd "${srcdir}/openslide-python-${pkgver}"
  python setup.py build

  cd "${srcdir}/openslide-python-${pkgver}-py2"
  python2 setup.py build
}

package_python-openslide() {
  depends=('openslide'
           'python-pillow')

  cd "${srcdir}/openslide-python-${pkgver}"
  python setup.py install \
    --root="${pkgdir}" \
    --optimize=1
}

package_python2-openslide() {
  depends=('openslide'
           'python2-pillow')

  cd "${srcdir}/openslide-python-${pkgver}-py2"
  python2 setup.py install \
    --root="${pkgdir}" \
    --optimize=1
}

# vim:set ts=2 sw=2 et:
