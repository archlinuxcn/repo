# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-threadpoolctl
_name=threadpoolctl
pkgver=1.1.0
pkgrel=1
pkgdesc='Python helpers to limit the number of threads used in native libraries that handle their own internal threadpool (BLAS and OpenMP implementations)'
arch=('any')
url='https://github.com/joblib/threadpoolctl'
license=('BSD')
makedepends=(
  'python-pip'
)
checkdepends=(
  'python-pytest'
)
source=(
  'https://github.com/joblib/threadpoolctl/raw/master/LICENSE'
  "https://files.pythonhosted.org/packages/py3/${_name::1}/${_name}/${_name/-/_}-${pkgver}-py3-none-any.whl"
)
md5sums=('8f2439cfddfbeebdb5cac3ae4ae80eaf'
         '290b79daaeb1832d73263450eb2479a1')

get_pyver () {
  python -c 'import sys; print(str(sys.version_info[0]) + "." + str(sys.version_info[1]))'
}

package() {
  PIP_CONFIG_FILE=/dev/null pip install --isolated --root="${pkgdir}" --ignore-installed --no-deps *.whl
  python -O -m compileall "${pkgdir}/usr/lib/python$(get_pyver)/site-packages/${_name}"
  install -Dm644 "${srcdir}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
