# Maintainer: Wil Thomason <wbthomason at cs dot cornell dot edu>

_pkgbase='python-fire'
pkgbase='python-fire'
pkgname=('python-fire')
pkgver='0.3.1'
pkgrel=1
pkgdesc='Python Fire is a library for automatically generating command line interfaces (CLIs) from
absolutely any Python object.'
arch=('any')
url='https://github.com/google/python-fire'
license=('Apache-2.0')
depends=('python' 'python-termcolor')
makedepends=('python-setuptools')
source=("https://github.com/google/python-fire/archive/v${pkgver}.tar.gz")
sha256sums=('b0728c4a59f48ff6d1a535ceff893ec1a79a7d68257fc0e6e3a40e1bef5773a0')

package_python-fire() {
    cd "${srcdir}/${_pkgbase}-${pkgver}"
    python setup.py install --root="${pkgdir}" --optimize=1
}
