# Maintainer: lilydjwg <lilydjwg@gmail.com>
# Modified From: python2-memoryprofiler by Rich Lindsley <richli.ff at gmail dot com>
pkgname=python-memoryprofiler
_py_pkgname=memory_profiler # The pypi package name
pkgver=0.31
pkgrel=1
pkgdesc="A module for monitoring memory usage of a python program. Python 3 version."
arch=('any')
url="http://pypi.python.org/pypi/memory_profiler"
license=('BSD')
depends=('python' 'python-psutil')
options=(!emptydirs)
source=(http://pypi.python.org/packages/source/m/$_py_pkgname/$_py_pkgname-$pkgver.tar.gz)

package() {
  cd "$srcdir/$_py_pkgname-$pkgver"
  python3 setup.py install --root="$pkgdir/" --optimize=1
  mv "$pkgdir/usr/bin/mprof" "$pkgdir/usr/bin/mprof3"
}

# vim:set ts=2 sw=2 et:

md5sums=('ab10ff2485a4258cd39237a0bf4b0295')
sha1sums=('884340c8dec155089ca5687eac47588e019f81d6')
sha256sums=('b492467608dc1a4594b7b578dc1aab46c1c926731baf293b1f494eeda0a1a35f')
