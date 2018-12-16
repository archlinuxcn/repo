# Contributor: Florian Klink <flokli at flokli dot de>

_python=python
_distname=pystache
pkgname=$_python-$_distname
pkgver=0.5.4
pkgrel=3
pkgdesc="The mustache template engine written in python"
arch=(any)
url="http://github.com/defunkt/pystache"
license=('MIT')
depends=('python' 'python-setuptools')
provides=('python-pystache')
conflicts=('python-pystache')
source=( "https://pypi.python.org/packages/source/${_distname:0:1}/$_distname/$_distname-$pkgver.tar.gz")
md5sums=('485885e67a0f6411d5252e69b20a35ca')

package() {
  cd "$srcdir/$_distname-$pkgver"
  $_python setup.py install --prefix=/usr --root="$pkgdir" --optimize=1 || exit 1
}
