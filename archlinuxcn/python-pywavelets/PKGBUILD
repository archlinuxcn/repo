# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Jingbei Li <i@jingbei.li>
# Contributor: Francois Boulogne <fboulogne at april dot org>
_base=pywavelets
pkgname=python-${_base}
pkgver=1.3.0
pkgrel=1
pkgdesc="Wavelet transform module"
arch=(x86_64)
url="https://github.com/${_base}/${_base::3}t"
license=(MIT)
depends=(python-numpy)
makedepends=(python-setuptools cython)
# checkdepends=(python-pytest python-matplotlib)
source=(${url}/archive/v${pkgver}.tar.gz)
sha512sums=('0a70ae2319ddd709a1fcd8d236d315ac7cfb68fbab69fc56cb51558038d5305787c1336496c942feaa66c9580b34a9bcb5aca91cdef20d8c4e22950ef60115cd')

build() {
  cd ${_base::3}t-${pkgver}
  export PYTHONHASHSEED=0
  python setup.py build
}

# check() {
#   cd ${_base::3}t-${pkgver}
#   python setup.py install --root="${srcdir}/tmp_install" --optimize=1 --skip-build
#   cd ${srcdir}
#   MPLBACKEND=Agg PYTHONPATH="${srcdir}/tmp_install/$(python -c "import site; print(site.getsitepackages()[0])")/${_base::3}t:${PYTHONPATH}" python -m pytest ${_base::3}t-${pkgver}/${_base::3}t/tests
# }

package() {
  cd ${_base::3}t-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python setup.py install --prefix=/usr --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
