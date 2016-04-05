_pkgname=tldextract
pkgname=python-tldextract
pkgver=2.0rc1
pkgrel=1
pkgdesc="Accurately separate the TLD from the registered domain andsubdomains of a URL, using the Public Suffix List."
arch=('any')
url="https://github.com/john-kurkowski/tldextract"
license=('BSD')
depends=('python' 'python-idna' 'python-setuptools')
source=('https://pypi.python.org/packages/source/t/tldextract/tldextract-2.0rc1.tar.gz')
md5sums=('5e853c274516a19064044a5c03253012')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"

  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
