# Maintainer: Wil Thomason <wbthomason at cs dot cornell dot edu>

_pkgbase='python-fire'
pkgbase='python-fire'
pkgname=('python-fire')
pkgver='0.4.0'
pkgrel=1
pkgdesc='Python Fire is a library for automatically generating command line interfaces (CLIs) from
absolutely any Python object.'
arch=('any')
url='https://github.com/google/python-fire'
license=('Apache-2.0')
depends=('python' 'python-termcolor')
makedepends=('python-setuptools')
source=("https://github.com/google/python-fire/archive/v${pkgver}.tar.gz")
sha256sums=('ea049aeec435e8630559b35d8bab949a1bb020ba0c1e92a039503b7d70ce0c47')

package_python-fire() {
    cd "${srcdir}/${_pkgbase}-${pkgver}"
    python setup.py install --root="${pkgdir}" --optimize=1
}
