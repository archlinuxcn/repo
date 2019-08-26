# Maintainer: Grey Christoforo <first name at last name dot net>

pkgname=python-pivy
_module='pivy'
pkgver=0.6.4
_RC="0.6.5a0"
_commit=406bc58e298d05f0847fc732f388c0993d28c0f8
pkgrel=2
pkgdesc="A Python binding for Coin"
url="https://github.com/FreeCAD/pivy"
depends=('python' 'coin' 'qt5-base' 'soqt')
makedepends=('python-setuptools' 'cmake' 'swig')
license=('BSD')
arch=('any')
#source=("https://github.com/FreeCAD/pivy/archive/${_RC}.tar.gz")
source=("https://github.com/FreeCAD/pivy/archive/${_commit}.tar.gz")
md5sums=('2f4565590b07d79346f1aef59a321a45')

prepare() {
    cd "$srcdir/${_module}-${_commit}"
    #touch cstddef cstdarg cassert
}

build() {
    cd "${srcdir}/${_module}-${_commit}"
    python setup.py build
}

package() {
    depends+=()
    cd "${srcdir}/${_module}-${_commit}"
    python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
