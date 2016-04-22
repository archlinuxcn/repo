_pkgname=tldextract
pkgname=python-tldextract
pkgver=2.0.0
pkgrel=1
pkgdesc="Accurately separate the TLD from the registered domain andsubdomains of a URL, using the Public Suffix List."
arch=('any')
url="https://github.com/john-kurkowski/tldextract"
license=('BSD')
depends=('python' 'python-idna' 'python-setuptools')
source=('https://pypi.python.org/packages/4d/f6/481eeb92a221879e2f90de3c85908bafc1f01babcb6f041f6918820da434/tldextract-2.0.0.tar.gz')
md5sums=('39340cec28261e0108d5bd7b37b3b004')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"

  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
