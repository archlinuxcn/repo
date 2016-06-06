_pkgname=requests-file
pkgname=python-requests-file
pkgver=1.4
pkgrel=1
pkgdesc="File transport adapter for Requests"
arch=('any')
url="http://github.com/dashea/requests-file"
license=('Apache')
depends=('python' 'python-requests' 'python-six' 'python-setuptools')
source=('https://pypi.python.org/packages/ff/1f/11aa5c35218501935e8e05e4ae52f72f416eeb69a9e8fe84e5ef660ccffb/requests-file-1.4.tar.gz')
md5sums=('fe475905d26986ee5fe77d9bcae3efcb')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"

  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
