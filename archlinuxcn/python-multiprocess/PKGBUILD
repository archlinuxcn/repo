# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Michel Zou <xantares09@hotmail.com>
_base=multiprocess
pkgname=python-${_base}
pkgdesc="better multiprocessing and multithreading in python"
pkgver=0.70.17
pkgrel=1
url="https://github.com/uqfoundation/${_base}"
arch=(any)
license=(BSD-3-Clause)
depends=(python-dill)
makedepends=(python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pytest python-tests)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('27431b17ad0ca3ffe5547a11e558969ec321bfc16d775de12f32a8125b9e2ca08986a123cdfc58095b980f53d7f169ad81fd601df5fcfbe3ed8f80948328364f')

build() {
  cd ${_base}-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

check() {
  cd ${_base}-${pkgver}
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  local _pyversion=$(python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
  test-env/bin/python -m pytest py${_pyversion}/${_base}/tests
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
