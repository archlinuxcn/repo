_pkgname=yarl
pkgname=python-yarl
pkgver=0.9.1
pkgrel=1
pkgdesc="Yet another URL library"
arch=('any')
url="https://github.com/aio-libs/yarl/"
license=('Apache')
depends=('python' 'python-multidict')
makedepends=('python-setuptools')
source=('https://pypi.python.org/packages/0f/60/d918b5593f4457ee3e7ef57eec5c4ddc403fa17a3035775a70a44ec6a490/yarl-0.9.1.tar.gz')
md5sums=('50e3ce72f00120734a2dd26fccbb35c6')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
