# Maintainer: Leo Mao <leomaoyw at gmail dot com>
pkgname=python-atari-py
_pkgname=atari-py
pkgver=0.2.6
pkgrel=2
pkgdesc="A python interface for the Arcade Learning Environment (Modified by OpenAI)"
arch=('any')
_github='openai/atari-py'
#_pypiname='atari-py'
url="https://github.com/openai/atari-py"
license=('GPL')
depends=('python' 'python-numpy' 'python-six' 'zlib')
makedepends=('python-setuptools' 'cmake' 'gcc')
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/openai/atari-py/archive/${pkgver}.tar.gz")
md5sums=('34c28ceac0813e74f5146c8e8333bf54')

build() {
  msg "Building Python 3"
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}"/ --optimize=1 --skip-build
}
