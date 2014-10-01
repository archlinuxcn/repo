# $Id: PKGBUILD 108513 2014-03-27 14:48:36Z fyan $
# Maintainer: Andrea Scarpino <andrea@archlinux.org>
# Contributor: examon <examon.mail[at]gmail[dot]com>
# Contributor: Sebastian Wiesner <lunaryorn googlemail com>
# Contributor: Dwight Schauer <dschauer@ti.com>

pkgbase=pypy-pyudev
pkgname=('pypy3-pyudev' 'pypy-pyudev')
pkgver=0.16.1
pkgrel=1
arch=('any')
url='http://pyudev.readthedocs.org/en/latest/index.html'
license=('LGPL')
makedepends=('pypy3-setuptools' 'pypy-setuptools')
source=("http://pypi.python.org/packages/source/p/pyudev/pyudev-${pkgver}.tar.gz")
md5sums=('4034de584b6d9efcbfc590a047c63285')

build() {
  cp -rf "${srcdir}/pyudev-${pkgver}" "${srcdir}/py2udev-${pkgver}"
}

package_pypy3-pyudev() {
  pkgdesc='A pure Python 3.x binding to libudev'
  depends=('pypy3>=2.3' 'pypy3<2.4' 'udev')

  cd pyudev-${pkgver}
  pypy3 setup.py install --root "${pkgdir}" --optimize=1
}

package_pypy-pyudev() {
  pkgdesc='A pure Python 2.x binding to libudev'
  depends=('pypy' 'udev')

  cd py2udev-${pkgver}
  pypy setup.py install --root "${pkgdir}" --optimize=1
}
