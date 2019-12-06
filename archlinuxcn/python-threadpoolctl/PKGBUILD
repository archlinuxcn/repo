# Maintainer: Butui Hu <hot123tea123@gmail.com>

_name=threadpoolctl
pkgname=python-threadpoolctl
pkgver=2.0.0
pkgrel=1
pkgdesc='Python helpers to limit the number of threads used in native libraries that handle their own internal threadpool (BLAS and OpenMP implementations)'
arch=(any)
url='https://github.com/joblib/threadpoolctl'
license=('BSD')
makedepends=(
  'python-setuptools'
)
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha256sums=('48b3e3e9ee079d6b5295c65cbe255b36a3026afc6dde3fb49c085cd0c004bbcf')

build() {
  cd "${srcdir}/${_name}-${pkgver}"
  python setup.py build
}

package() {
  cd "${srcdir}/${_name}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
# vim:set ts=2 sw=2 et:

