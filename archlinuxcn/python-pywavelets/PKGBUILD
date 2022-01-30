# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Jingbei Li <i@jingbei.li>
# Contributor: Francois Boulogne <fboulogne at april dot org>
_base=pywavelets
pkgname=python-${_base}
pkgver=1.2.0
pkgrel=1
pkgdesc="Wavelet transform module"
arch=(x86_64)
url="https://github.com/${_base}/${_base::3}t"
license=(MIT)
depends=(python-numpy)
makedepends=(python-setuptools cython)
# checkdepends=(python-pytest python-matplotlib)
source=(${url}/archive/v${pkgver}.tar.gz)
sha512sums=('a999f7b316a434948ab06f33ab7aeea621b7e33bfc0907ea396da40482f896aa8688627873741cf3abf01f098b21515cffad42b4e966a431347cb5f013e78752')

build() {
  cd ${_base::3}t-${pkgver}
  export PYTHONHASHSEED=0
  python setup.py build
}

# check() {
#   local _pyversion=$(python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
#   MPLBACKEND=Agg PYTHONPATH="${_base::3}t-${pkgver}/build/lib.linux-${CARCH}-${_pyversion}:${PYTHONPATH}" python -m pytest --pyargs ${_base::3}t-${pkgver}/${_base::3}t
# }

package() {
  cd ${_base::3}t-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python setup.py install --prefix=/usr --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
