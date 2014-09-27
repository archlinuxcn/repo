# $Id: PKGBUILD 108452 2014-03-27 14:47:51Z fyan $
# Maintainer: Evangelos Foutras <evangelos@foutrelis.com>
# Contributor: Peter Baldwin <bald_pete@hotmail.com>

pkgbase='pypy-jinja'
pkgname='pypy-jinja'
pkgname=('pypy3-jinja' 'pypy-jinja')
pkgver=2.7.2
pkgrel=4
pkgdesc="A simple pythonic template language written in Python"
arch=('any')
url="http://jinja.pocoo.org/"
license=('BSD')
makedepends=('pypy-setuptools' 'pypy3-setuptools' 'pypy-markupsafe'
             'pypy3-markupsafe')
source=(http://pypi.python.org/packages/source/J/Jinja2/Jinja2-$pkgver.tar.gz)
sha256sums=('310a35fbccac3af13ebf927297f871ac656b9da1d248b1fe6765affa71b53235')

build() {
  cd "$srcdir"

  rm -rf pypy{,3}-build
  for builddir in pypy{,3}-build; do
    cp -r Jinja2-$pkgver $builddir
    pushd $builddir
    ${builddir%-build} setup.py build
    popd
  done
}

package_pypy3-jinja() {
  depends=('pypy3-setuptools' 'pypy3-markupsafe' "pypy3>=2.3" "pypy3<=2.4")

  cd "$srcdir/pypy3-build"

  # pypy3 setup.py install --root="$pkgdir" -O1 \
  #   --install-lib=/opt/pypy3/lib/python3.2/site-packages
  pypy3 setup.py install --root="$pkgdir" -O1

  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_pypy-jinja() {
  depends=('pypy-setuptools' 'pypy-markupsafe' "pypy>=2.3" "pypy<=2.4")

  cd "$srcdir/pypy-build"

  pypy setup.py install --root="$pkgdir" -O1

  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
