# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Michel Zou <xantares09@hotmail.com>
_base=multiprocess
pkgname=python-${_base}
pkgdesc="better multiprocessing and multithreading in python"
pkgver=0.70.16
pkgrel=2
url="https://github.com/uqfoundation/${_base}"
arch=(any)
license=(BSD-3-Clause)
depends=(python-dill)
makedepends=(python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pytest python-tests)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('b38d0337e1b90ed43c3c8877d7ce3c5729950fd8f1ad8cd4561ece12848eff7ca7d8769f7cef3508735e16c1c2d76d1b17439f275ca52f9c13117e9346e645fa')

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
