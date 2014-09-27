# $Id: PKGBUILD 108502 2014-03-27 14:48:28Z fyan $
# Maintainer: Sébastien Luttringer
# Contributor: Angel Velasquez <angvp@archlinux.org>
# Contributor: Fabio Volpe <volpefabio@gmail.com>

pkgbase=pypy-sphinx
pkgname=('pypy3-sphinx' 'pypy-sphinx')
pkgver=1.2.2
pkgrel=3
arch=('any')
url='http://sphinx.pocoo.org/'
license=('GPL')
makedepends=(
  'pypy3-setuptools'
  'pypy3-docutils'
  'pypy3-jinja'
  'pypy3-pygments'
  'pypy-setuptools'
  'pypy-docutils'
  'pypy-jinja'
  'pypy-pygments'
)
checkdepends=(
  'pypy3-nose'
  'pypy-nose'
  'texlive-latexextra'
)
source=("http://pypi.python.org/packages/source/S/Sphinx/Sphinx-$pkgver.tar.gz")
md5sums=('3dc73ccaa8d0bfb2d62fb671b1f7e8a4')

prepare() {
  # souce duplication is required because makefile modify source code
  # setyp.py --build tricks don't works well
  cp -a Sphinx-$pkgver Sphinx-${pkgver}2

  # change pypy interpreter
  find Sphinx-${pkgver}2 -type f -exec \
    sed -i '1s,^#! \?/usr/bin/\(env \|\)python$,#!/usr/bin/pypy,' {} \;

  # change sphinx-binaries name in source code
  find Sphinx-${pkgver}2 -type f -name '*.py' -exec \
    sed -ri 's,(sphinx-(:?build|apidoc|autogen|quickstart)),\1-pypy,' {} \;

  # change pypy interpreter
  find Sphinx-${pkgver} -type f -exec \
    sed -i '1s,^#! \?/usr/bin/\(env \|\)python$,#!/usr/bin/pypy3,' {} \;

  # change sphinx-binaries name in source code
  find Sphinx-${pkgver} -type f -name '*.py' -exec \
    sed -ri 's,(sphinx-(:?build|apidoc|autogen|quickstart)),\1-pypy3,' {} \;
}

build() {
  msg2 'PyPy 3 version'
  cd "$srcdir"/Sphinx-$pkgver
  make PYTHON=pypy3 build

  msg2 'PyPy 2 version'
  cd "$srcdir"/Sphinx-${pkgver}2
  make PYTHON=pypy build
}

check() {
  msg2 'PyPy 3 version'
  cd "$srcdir"/Sphinx-$pkgver
  make PYTHON=pypy3 test

  msg2 'PyPy 2 version'
  cd "$srcdir"/Sphinx-${pkgver}2
  make PYTHON=pypy test
}

package_pypy3-sphinx() {
  pkgdesc='Pypy3 documentation generator'
  depends=('pypy3-jinja' 'pypy3-pygments' 'pypy3-docutils')
  optdepends=('texlive-latexextra: for generation of PDF documentation')

  cd Sphinx-$pkgver
  pypy3 setup.py install --root="$pkgdir" --optimize=1

  install -dm755 "${pkgdir}/usr"
  mv "${pkgdir}/opt/pypy3/bin" "${pkgdir}/usr"
}

package_pypy-sphinx() {
  pkgdesc='Pypy documentation generator'
  depends=('pypy-jinja' 'pypy-pygments' 'pypy-docutils')
  optdepends=('texlive-latexextra: for generation of PDF documentation')

  cd Sphinx-${pkgver}2
  pypy setup.py install --root="$pkgdir" --optimize=1

  install -dm755 "${pkgdir}/usr"
  mv "${pkgdir}/opt/pypy/bin" "${pkgdir}/usr"
}
