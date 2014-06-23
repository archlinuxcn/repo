# $Id: PKGBUILD 108505 2014-03-27 14:48:31Z fyan $
# Maintainer: Felix Yan <felixonmars@gmail.com>
# Contributor: Stéphane Gaudreault <stephane@archlinux.org>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: Angel 'angvp' Velasquez <angvp[at]archlinux.com.ve>  
# Contributor: Peter Garceau <RockyChimp@gmail.com>

pkgbase=pypy-sympy
pkgname=('pypy3-sympy' 'pypy-sympy')
pkgver=0.7.5
pkgrel=2
arch=('any')
pkgdesc='Symbolic manipulation package (Computer Algebra System), written in pure Python'
url='http://sympy.org/en/index.html'
license=('BSD')
makedepends=('pypy' 'pypy3' 'git')
source=("https://github.com/sympy/sympy/releases/download/sympy-${pkgver}/sympy-${pkgver}.tar.gz")
md5sums=('7de1adb49972a15a3dd975e879a2bea9')

prepare() {
  cp -r sympy-${pkgver} py3-sympy-${pkgver}

  sed -i -e 's|#!/usr/bin/env python|#!/usr/bin/env pypy|' \
         -e 's|#!/usr/bin/python|#!/usr/bin/pypy|' \
    sympy-${pkgver}/sympy/mpmath/tests/{runtests.py,test_eigen.py,test_levin.py,test_eigen_symmetric.py} \
    sympy-${pkgver}/sympy/mpmath/matrices/{eigen.py,eigen_symmetric.py} \
    sympy-${pkgver}/sympy/utilities/tests/diagnose_imports.py

  sed -i -e 's|#!/usr/bin/env python|#!/usr/bin/env pypy3|' \
         -e 's|#!/usr/bin/python|#!/usr/bin/pypy3|' \
    py3-sympy-${pkgver}/sympy/mpmath/tests/{runtests.py,test_eigen.py,test_levin.py,test_eigen_symmetric.py} \
    py3-sympy-${pkgver}/sympy/mpmath/matrices/{eigen.py,eigen_symmetric.py} \
    py3-sympy-${pkgver}/sympy/utilities/tests/diagnose_imports.py
}

build() {
  cd sympy-${pkgver}
  pypy setup.py build

  cd ../py3-sympy-${pkgver}
  pypy3 setup.py build
}

package_pypy-sympy() {
  depends=('pypy')
  optdepends=('pypy-pyglet: plotting'
              'pypy-ipython: user friendly interface for isympy')

  cd sympy-${pkgver}

  pypy setup.py install --skip-build --root "${pkgdir}" --optimize=1

  install -m755 -d "${pkgdir}/usr"
  mv "$pkgdir/opt/pypy/"{share,bin} "$pkgdir/usr/"

  # rename files that exists in both 'python2-sympy' and 'python-sympy'
  mv "${pkgdir}"/usr/bin/isympy{,-pypy}
  mv "${pkgdir}"/usr/share/man/man1/isympy{,-pypy}.1

  install -D -m644 LICENSE "${pkgdir}"/usr/share/licenses/${pkgname}/LICENSE
}

package_pypy3-sympy() {
  depends=("pypy3>=2.3" "pypy3<=2.4")
  optdepends=('pypy-ipython: user friendly interface for isympy')

  cd py3-sympy-${pkgver}

  # pypy3 setup.py install --skip-build --root "${pkgdir}" --optimize=1 \
  #   --install-lib=/opt/pypy3/lib/python3.2/site-packages
  pypy3 setup.py install --skip-build --root "${pkgdir}" --optimize=1

  install -m755 -d "${pkgdir}/usr"
  mv "$pkgdir/opt/pypy3/"{share,bin} "$pkgdir/usr/"

  # rename files that exists in both 'python2-sympy' and 'python-sympy'
  mv "${pkgdir}"/usr/bin/isympy{,-pypy3}
  mv "${pkgdir}"/usr/share/man/man1/isympy{,-pypy3}.1

  install -D -m644 LICENSE "${pkgdir}"/usr/share/licenses/${pkgname}/LICENSE
}
