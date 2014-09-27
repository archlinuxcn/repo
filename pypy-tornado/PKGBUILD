# $Id: PKGBUILD 110749 2014-05-06 04:31:01Z fyan $
# Maintainer: Felix Yan <felixonmars@gmail.com>
# Contributor: Thomas Dziedzic < gostrc at gmail >

pkgbase='pypy-tornado'
pkgname=('pypy3-tornado' 'pypy-tornado')
pkgver=4.0.0
pkgrel=1
pkgdesc='open source version of the scalable, non-blocking web server and tools'
arch=('i686' 'x86_64')
url='http://www.tornadoweb.org/'
license=('Apache')
makedepends=('pypy-setuptools' 'pypy3-setuptools'
  'pypy-backports.ssl_match_hostname' 'pypy-certifi' 'pypy3-certifi')
source=(https://github.com/facebook/tornado/archive/v${pkgver}.tar.gz)
md5sums=('fa1592ec213a4d265af23fdc0b14c989')

prepare() {
  cp -a tornado-${pkgver}{,-py2}

  # python -> python2 rename
  find tornado-${pkgver}-py2 -name '*py' \
    -exec sed -e 's_#!/usr/bin/env python_#!/usr/bin/env pypy_' -i {} \;
  find tornado-${pkgver} -name '*py' \
    -exec sed -e 's_#!/usr/bin/env python_#!/usr/bin/env pypy3_' -i {} \;
}

build() {
  cd tornado-${pkgver}
  pypy3 setup.py build

  cd ../tornado-${pkgver}-py2
  pypy setup.py build
}

package_pypy3-tornado() {
  depends=("pypy3>=2.3" "pypy3<=2.4")

  cd tornado-${pkgver}
  pypy3 setup.py install --skip-build --root="${pkgdir}" --optimize=1
}

package_pypy-tornado() {
  depends=('pypy' 'pypy-backports.ssl_match_hostname')

  cd tornado-${pkgver}-py2
  pypy setup.py install --skip-build --root="${pkgdir}" --optimize=1
}
