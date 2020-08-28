# Maintainer: Jerry Lin <jerry73204 at gmail dot com>

pkgname='python-fvcore'
pkgver=0.1.1.post200513
pkgrel=1
pkgdesc="Collection of common code that's shared among different research projects in FAIR computer vision team."
arch=('any')
url="https://github.com/facebookresearch/fvcore"
license=('Apache')
makedepends=('python-setuptools' 'python2-setuptools')
depends=('python')
source=("https://files.pythonhosted.org/packages/43/3a/50bb1e1b1acbf5e9b79f9f0c078cd3e9694e453a61cd0f07cc8dd1e1872f/fvcore-${pkgver}.tar.gz")
sha256sums=('fa9cb6daa6912d05bc03ccb1e15adf5c1bde5c308c34379102515e36f6379b30')

_dirname="fvcore-${pkgver}"

build() {
  cd "${srcdir}/${_dirname}"
  python setup.py build
}

package() {
  cd "${srcdir}/${_dirname}"
  python setup.py install --root="$pkgdir" --optimize=1
}
