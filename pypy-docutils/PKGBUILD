# $Id: PKGBUILD 115222 2014-07-07 00:43:25Z seblu $
# Maintainer: Sébastien Luttringer
# Contributor : Ionut Biru <ibiru@archlinux.org>
# Contributor: Sergej Pupykin <pupykin.s+arch@gmail.com>

pkgbase=pypy-docutils
pkgname=('pypy3-docutils' 'pypy-docutils')
pkgver=0.12
pkgrel=1
pkgdesc='Set of tools for processing plaintext docs into formats such as HTML, XML, or LaTeX'
arch=('any')
url='http://docutils.sourceforge.net'
license=('custom')
makedepends=('pypy3' 'pypy')
source=("http://downloads.sourceforge.net/docutils/docutils-$pkgver.tar.gz"
        '01-rst2odt_prepstyles-elementtree.patch')
md5sums=('4622263b62c5c771c03502afa3157768'
         '34952e8a50692b628a8aa2dde3072f07')

build() {
  cd docutils-$pkgver
  msg2 01-rst2odt_prepstyles-elementtree.patch
  patch -p1 -i "$srcdir"/01-rst2odt_prepstyles-elementtree.patch

  msg2 pypy3
  pypy3 setup.py build --build-lib=build/pypy3
  find build/pypy3 -type f -exec \
    sed -i '1s,^#! \?/usr/bin/\(env \|\)python$,#!/usr/bin/pypy3,' {} \;

  msg2 pypy
  pypy setup.py build --build-lib=build/pypy
  find build/pypy -type f -exec \
    sed -i '1s,^#! \?/usr/bin/\(env \|\)python$,#!/usr/bin/pypy,' {} \;
}

check() {
  cd docutils-$pkgver
  # we need utf locale to valid utf8 tests
  export LANG=en_US.UTF-8

  # Disable pypy check

  # msg2 'pypy3 checks'
  # PYTHONPATH="$PWD/build/pypy3/" pypy3 test3/alltests.py
  # msg2 'pypy checks'
  # PYTHONPATH="$PWD/build/pypy/" pypy test/alltests.py
}

package_pypy3-docutils() {
  depends=('pypy3>=2.3' 'pypy3<=2.4')

  cd docutils-$pkgver
  pypy3 setup.py build --build-lib=build/pypy3 \
    install --root="$pkgdir" --optimize=1

  install -dm755 "${pkgdir}/usr"
  mv "${pkgdir}/opt/pypy3/bin" "${pkgdir}/usr"

  # fix python-docutils conflict
  for _f in "$pkgdir"/usr/bin/*.py; do
      mv -v "$_f" "${_f%.py}-pypy3.py"
  done

  # symlink without .py
  for f in "$pkgdir"/usr/bin/*.py; do
      ln -s "$(basename $f)" "$pkgdir/usr/bin/$(basename $f .py)"
  done

  # setup license
  install -D -m644 COPYING.txt "$pkgdir/usr/share/licenses/$pkgname/COPYING.txt"
  install -D -m644 licenses/python* "$pkgdir/usr/share/licenses/$pkgname/"
}

package_pypy-docutils() {
  depends=('pypy')

  cd docutils-$pkgver
  pypy setup.py build --build-lib=build/pypy \
    install --root="$pkgdir" --optimize=1

  install -dm755 "${pkgdir}/usr"
  mv "${pkgdir}/opt/pypy/bin" "${pkgdir}/usr"

  # fix python-docutils conflict
  for _f in "$pkgdir"/usr/bin/*.py; do
      mv -v "$_f" "${_f%.py}-pypy.py"
  done

  # symlink without .py
  for _f in "$pkgdir"/usr/bin/*.py; do
      ln -s "$(basename $_f)" "$pkgdir/usr/bin/$(basename $_f .py)"
  done

  # setup license
  install -D -m644 COPYING.txt "$pkgdir/usr/share/licenses/$pkgname/COPYING.txt"
  install -D -m644 licenses/python* "$pkgdir/usr/share/licenses/$pkgname/"
}
