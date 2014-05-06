# $Id: PKGBUILD 110749 2014-05-06 04:31:01Z fyan $
# Maintainer: Felix Yan <felixonmars@gmail.com>
# Contributor: Thomas Dziedzic < gostrc at gmail >

pkgbase='pypy-tornado'
true && pkgname=('pypy-tornado' 'pypy3-tornado')
pkgname='pypy-tornado'
pkgver=3.2.1
pkgrel=1
pkgdesc='open source version of the scalable, non-blocking web server and tools'
arch=('i686' 'x86_64')
url='http://www.tornadoweb.org/'
license=('Apache')
makedepends=('git')
source=(https://github.com/facebook/tornado/archive/v3.2.1.tar.gz)
md5sums=('1c8910c1f6476ab947e6a5136a9961c9')

prepare() {
  cp -a tornado{,-py2}

  # python -> python2 rename
  find tornado-py2 -name '*py' \
    -exec sed -e 's_#!/usr/bin/env python_#!/usr/bin/env pypy_' -i {} \;
  find tornado -name '*py' \
    -exec sed -e 's_#!/usr/bin/env python_#!/usr/bin/env pypy3_' -i {} \;
}

build() {
  cd tornado
  pypy3 setup.py build

  cd ../tornado-py2
  pypy setup.py build
}

package_pypy3-tornado() {
  depends=('pypy3')

  cd tornado
  pypy3 setup.py install --root="${pkgdir}" --optimize=1
}

package_pypy-tornado() {
  depends=('pypy')

  cd tornado-py2
  pypy setup.py install --root="${pkgdir}" --optimize=1
}
