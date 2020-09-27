# Maintainer: Grey Christoforo <first name [at] last name [dot] net>

pkgname=python-pyvisa-py
pkgver=0.5.0
pkgrel=2
pkgdesc="A pure python backend for PyVISA"
arch=('any')
license=('MIT')
depends=('python' 'python-pyvisa')
makedepends=('python-setuptools-scm')
conflicts=('python-pyvisa-py-git')

source=(https://github.com/pyvisa/pyvisa-py/archive/${pkgver}.tar.gz)
md5sums=('5fa46bd2eda3b8f2893caea1f2219447')
url="https://github.com/pyvisa/pyvisa-py"

prepare() {
  cd "pyvisa-py-${pkgver}"
  sed "/^author =.*/i version = ${pkgver}" -i setup.cfg
  sed -i "s,use_scm_version=True,use_scm_version=False,g" setup.py

  sed '/\[tool.setuptools_scm\]/d' -i pyproject.toml

  # fix serial device name bug
  curl https://patch-diff.githubusercontent.com/raw/pyvisa/pyvisa-py/pull/269.patch | patch -p1

  # fix broken serial writes
  curl https://patch-diff.githubusercontent.com/raw/greyltc/pyvisa-py/pull/1.patch | patch -p1
}

package() {
  cd pyvisa-py-${pkgver}
  python setup.py install --prefix=/usr --root="$pkgdir/" --optimize=1
}

# vim:set ts=2 sw=2 et:
