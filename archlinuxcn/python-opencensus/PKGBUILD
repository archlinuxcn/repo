# Maintainer: acxz <akashpatel2008 at yahoo dot com>

pkgname=python-opencensus
pkgver=0.7.12
pkgrel=1
pkgdesc='A stats collection and distributed tracing framework'
arch=('any')
url='https://github.com/census-instrumentation/opencensus-python'
license=('Apache-2.0')
depends=('python' 'python-google-api-core')
makedepends=('python-setuptools')
source=("$pkgname-$pkgver.tar.gz::https://github.com/census-instrumentation/opencensus-python/archive/v$pkgver.tar.gz")
sha256sums=('9cc162037bff19b46e65a394b67ac9821ea9b86fed6d7371f5365e538418a8b8')

_pkgname=opencensus-python

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}/context/opencensus-context"
  python setup.py build

  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}/context/opencensus-context"
  python setup.py install --root="$pkgdir"/ --optimize=1

  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py install --root="$pkgdir"/ --optimize=1
}
