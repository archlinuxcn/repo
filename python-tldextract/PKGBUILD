_pkgname=tldextract
pkgname=python-tldextract
pkgver=2.0.1
pkgrel=1
pkgdesc="Accurately separate the TLD from the registered domain andsubdomains of a URL, using the Public Suffix List."
arch=('any')
url="https://github.com/john-kurkowski/tldextract"
license=('BSD')
depends=('python' 'python-idna' 'python-setuptools')
source=('https://pypi.python.org/packages/f4/fd/f9995517d2fce9b4800680916c8ace079cf6ced8fb7ff84a301105d87668/tldextract-2.0.1.tar.gz')
md5sums=('b5ac6436f4b25c802bb59d253848f897')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"

  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
