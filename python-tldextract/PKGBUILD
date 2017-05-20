_pkgname=tldextract
pkgname=python-tldextract
pkgver=2.0.3
pkgrel=1
pkgdesc="Accurately separate the TLD from the registered domain and subdomains of a URL, using the Public Suffix List. Bydefault, this includes the public ICANN TLDs and theirexceptions. You can optionally support the Public SuffixList's private domains as well."
arch=('any')
url="https://github.com/john-kurkowski/tldextract"
license=('BSD')
depends=('python' 'python-idna' 'python-requests-file' 'python-setuptools')
source=('https://pypi.python.org/packages/32/fe/e6f010a97ea48e802038b083a7316fa28fbaad843eacfbd12637d9d221a2/tldextract-2.0.3.tar.gz')
md5sums=('028176cf2245e4baac0601fe99796906')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build

  _pyver=$(python -c 'import sysconfig; print(sysconfig.get_python_version())')
  # use the snapshot version, because generating a new one requires Internat access and root permission
  ln -s .tld_set_snapshot "$pkgdir/usr/lib/python$_pyver/site-packages/tldextract/.tld_set"

}

# vim:set sw=2 et:
