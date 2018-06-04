_pkgname=butterfly
pkgname=butterfly
pkgver=3.2.3
pkgrel=1
pkgdesc="A sleek web based terminal emulator"
arch=('any')
url="https://github.com/paradoxxxzero/butterfly"
license=('GPLv3')
depends=('python' 'python-pyopenssl' 'python-tornado' 'tornado_systemd' 'python-setuptools')
optdepends=('python-libsass')
source=('https://files.pythonhosted.org/packages/23/7a/4a1f5b93448fc5e7a187c99a06612df6a4fa727baac5514c2f13326be4e0/butterfly-3.2.3.tar.gz')
md5sums=('431f750cc526b9e32cd39eefe543bd5e')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
