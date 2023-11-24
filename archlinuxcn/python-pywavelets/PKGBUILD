# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Jingbei Li <i@jingbei.li>
# Contributor: Francois Boulogne <fboulogne at april dot org>
_base=pywavelets
pkgname=python-${_base}
pkgver=1.5.0
pkgrel=1
pkgdesc="Wavelet transform module"
arch=(x86_64)
url="https://github.com/${_base}/${_base::3}t"
license=(MIT)
depends=(python-numpy)
makedepends=(python-build python-installer meson-python python-setuptools python-wheel cython)
# checkdepends=(python-pytest python-matplotlib) # python-scipy
source=(${_base::3}t-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('b430c6adf941fe5d1e63d42f5bd6861ddf5a1c6eab95e3731e96466cb98f6f1bc463c699ebfceeb97ec6a11c9c396296a3729e23a4e5bf8fbf49c31745a62dfe')

build() {
  cd ${_base::3}t-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

# check() {
#   python -m venv --system-site-packages test-env
#   test-env/bin/python -m installer ${_base::3}t-${pkgver}/dist/*.whl
#   MPLBACKEND=Agg test-env/bin/python -m pytest --pyargs ${_base::3}t-${pkgver}/${_base::3}t/tests
# }

package() {
  cd ${_base::3}t-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
