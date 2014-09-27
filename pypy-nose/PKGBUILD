# $Id: PKGBUILD 212103 2014-05-07 13:57:27Z dan $
# Maintainer: Dan McGee <dan@archlinux.org>
# Contributor: Angel Velasquez <angvp@archlinux.org>
# Contributor: Douglas Soares de Andrade <douglas@archlinux.org>
# Contributor: Cilyan Olowen <gaknar@gmail.com>

pkgbase=pypy-nose
pkgname=('pypy3-nose' 'pypy-nose' 'pypy-nose-doc')
pkgver=1.3.3
pkgrel=1
pkgdesc="A discovery-based unittest extension"
arch=('any')
url='http://readthedocs.org/docs/nose/'
license=('LGPL2.1')
makedepends=('pypy' 'pypy-setuptools' 'pypy3' 'pypy-setuptools' 'pypy-sphinx')
source=("http://pypi.python.org/packages/source/n/nose/nose-${pkgver}.tar.gz")
md5sums=('42776061bf5206670cb819176dc78654')

build() {
  cd "$srcdir/nose-$pkgver"
  sed -i -e "s:man/man1:share/man/man1:g" setup.py
  cp -R "$srcdir/nose-$pkgver" "$srcdir/nose2-$pkgver"

  cd "$srcdir/nose-$pkgver"
  pypy3 setup.py build

  cd "$srcdir/nose2-$pkgver"
  pypy setup.py build
}

package_pypy3-nose() {
  depends=('pypy3<2.4' 'pypy3>=2.3' 'pypy3-setuptools')

  cd "$srcdir/nose-$pkgver"
  pypy3 setup.py install --root="${pkgdir}" -O1 --skip-build

  install -dm755 "${pkgdir}/usr"
  mv "${pkgdir}/opt/pypy3/bin" "${pkgdir}/usr"
  mv "$pkgdir/usr/bin/nosetests" "$pkgdir/usr/bin/nosetests-pypy3"
  mv "$pkgdir/usr/bin/nosetests-3.2" "$pkgdir/usr/bin/nosetests-pypy3.2"
}

package_pypy-nose() {
  depends=('pypy' 'pypy-setuptools')
  cd "$srcdir/nose2-$pkgver"
  pypy setup.py install --root="${pkgdir}" -O1 --skip-build

  install -dm755 "${pkgdir}/usr"
  mv "${pkgdir}/opt/pypy/bin" "${pkgdir}/usr"
  mv "$pkgdir/usr/bin/nosetests" "$pkgdir/usr/bin/nosetests-pypy"
  mv "$pkgdir/usr/bin/nosetests-2.7" "$pkgdir/usr/bin/nosetests-pypy2.7"
  rm -rf "$pkgdir/usr/share"
}

package_pypy-nose-doc(){
  pkgdesc="Nose documentation and examples"
  provides=('python-nose-doc')
  conflicts=('python-nose-doc')

  cd "$srcdir/nose-$pkgver/doc"
  make SPHINXBUILD=sphinx-build2 html
  mkdir -p "$pkgdir/usr/share/doc/python-nose"
  cp -r .build/html "$pkgdir/usr/share/doc/python-nose"
  cp -r ../examples "$pkgdir/usr/share/doc/python-nose"
}
