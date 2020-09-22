# Maintainer: Greyson Christoforo <grey@christoforo.net>
# Contributor: Alex Forencich <alex@alexforencich.com>
pkgname=python-pyvisa 
pkgver=1.11.0
pkgrel=1
pkgdesc="A Python package with bindings to the 'Virtual Instrument Software Architecture' VISA library"
arch=('any')
url="https://github.com/pyvisa/pyvisa"
license=('MIT')
depends=('python' 'python-distribute' 'python-docutils' 'python-setuptools-scm')
optdepends=('python-pyvisa-py: Pure Python backend')

source=("https://github.com/pyvisa/pyvisa/archive/$pkgver.tar.gz")
md5sums=('1922d2631d370c4dd83118da22842d76')

prepare() {
  cd "pyvisa-${pkgver}"
  sed "/^author =.*/i version = ${pkgver}" -i setup.cfg
  sed -i "s,use_scm_version=True,use_scm_version=False,g" setup.py

  sed '/\[tool.setuptools_scm\]/d' -i pyproject.toml
}

build() {
  cd "pyvisa-${pkgver}"
  python setup.py build
}

package(){
  cd "pyvisa-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}

