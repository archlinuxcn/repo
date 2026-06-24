# Maintainer: Yakov Till <yakov.till@gmail.com>

_name=signxml
pkgname=python-signxml
pkgver=5.0.1
pkgrel=1
pkgdesc="Python XML Signature and XAdES library"
arch=(any)
url="https://github.com/XML-Security/signxml"
license=(Apache-2.0)
depends=(python python-certifi python-cryptography python-lxml)
makedepends=(python-build python-installer python-hatchling python-hatch-vcs)
checkdepends=(python-pytest)
optdepends=('python-pyinstaller: collect signxml data files when freezing apps')
source=(${_name}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/s/signxml/signxml-${pkgver}.tar.gz)
sha256sums=('996d1740358d9fffc4429dc99284b4ff522bc38dde57e41f1d5c8c365d56c107')

latestver() {
  curl -fsSL 'https://pypi.org/pypi/signxml/json' | jq -r '.info.version'
}

build() {
  cd "$_name-$pkgver"
  python -m build --wheel --no-isolation
}

check() {
  cd "$_name-$pkgver"
  rm -rf test-env
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  test-env/bin/python -m pytest -vv test/test.py
}

package() {
  cd "$_name-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
