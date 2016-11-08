_pkgname=yarl
pkgname=python-yarl
pkgver=0.7.0
pkgrel=1
pkgdesc="Yet another URL library"
arch=('any')
url="https://github.com/aio-libs/yarl/"
license=('Apache')
depends=('python' 'python-multidict')
makedepends=('python-setuptools')
source=('https://pypi.python.org/packages/6a/09/c7213413ea440e489d13aa53c6ffc80b532070d28a0a75cf56691eaf522e/yarl-0.7.0.tar.gz')
md5sums=('d658c903a4666979913a7487c1d06574')

export LANG=en_US.UTF-8

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"

  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
