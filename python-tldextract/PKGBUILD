_pkgname=tldextract
pkgname=python-tldextract
pkgver=2.1.0
pkgrel=2
pkgdesc="Accurately separate the TLD from the registered domain and subdomains of a URL, using the Public Suffix List"
arch=('any')
url="https://github.com/john-kurkowski/tldextract"
license=('BSD')
depends=('python' 'python-idna' 'python-requests-file' 'python-setuptools')
source=('https://pypi.python.org/packages/15/8c/6c852f0dd1cc6ddd43d4eb8b67b78a099d6b8e25d6144f85bdfb08df9645/tldextract-2.1.0.tar.gz')
md5sums=('f0c54bebd3e1a4ac64df16a603c56bd2')

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
