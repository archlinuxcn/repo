_pkgname=tldextract
pkgname=python-tldextract
pkgver=1.7.5
pkgrel=2
pkgdesc="Accurately separate the TLD from the registered domain andsubdomains of a URL, using the Public Suffix List."
arch=('any')
url="https://github.com/john-kurkowski/tldextract"
license=('BSD')
depends=('python' 'python-idna' 'python-setuptools')
source=('https://pypi.python.org/packages/source/t/tldextract/tldextract-1.7.5.tar.gz')
md5sums=('1bd2e3ba0b49ce46e9eeb9d5e6d77245')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"

  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
