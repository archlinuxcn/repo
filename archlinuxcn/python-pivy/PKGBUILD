# Maintainer: Grey Christoforo <first name at last name dot net>

pkgname=python-pivy
_module='pivy'
pkgver=0.6.5
pkgrel=1
pkgdesc="A Python binding for Coin"
url="http://pivy.coin3d.org/"
depends=('python' 'coin' 'qt5-base' 'glu')
makedepends=('python-setuptools' 'cmake' 'swig')
license=('BSD')
arch=('any')
source=("https://github.com/FreeCAD/pivy/archive/${pkgver}.tar.gz")
md5sums=('73b6083aa1c055c83294d0fa1fee037b')

prepare() {
    cd "$srcdir/${_module}-${pkgver}/fake_headers"
    touch cstddef cstdarg cassert
}

build() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py build
}

package() {
    depends+=()
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
