_pkgname=tldextract
pkgname=python-tldextract
pkgver=2.0.2
pkgrel=1
pkgdesc="Accurately separate the TLD from the registered domain andsubdomains of a URL, using the Public Suffix List."
arch=('any')
url="https://github.com/john-kurkowski/tldextract"
license=('BSD')
depends=('python' 'python-idna' 'python-requests-file' 'python-setuptools')
source=('https://pypi.python.org/packages/44/db/ab27d3003968f766bff7bde238de418d2b8ddd727c3e56346ffd3ef05e27/tldextract-2.0.2.tar.gz')
md5sums=('bcc6a198864f9c86ffdd8014fa3ccd73')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"

  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
