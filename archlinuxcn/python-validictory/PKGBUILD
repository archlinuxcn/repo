# Maintainer: Solomon Choina <shlomochoina@gmail.com>
pkgname='python-validictory'
_module='validictory'
pkgver='1.1.2'
pkgrel=2
pkgdesc="general purpose python data validator"
url="http://github.com/jamesturk/validictory"
depends=('python')
makedepends=('python-setuptools')
license=('BSD')
arch=('any')
source=("https://files.pythonhosted.org/packages/source/v/validictory/validictory-${pkgver}.tar.gz")
sha256sums=('3a87b84658592f75f37d6bab77ac223774c9989dc7349c8aad19a424770835ba')

build() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py build
}

package() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
