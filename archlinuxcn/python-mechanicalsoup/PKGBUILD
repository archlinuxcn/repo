# Maintainer: Colin Arnott <colin@urandom.co.uk>
# Contributer: Jonathan Arnold <jdarnold@archlinux.us>
# Contributor: Zhang Hai <dreaming.in.code.zh@gmail.com>

pkgbase=python-mechanicalsoup
pkgname=(python-mechanicalsoup python2-mechanicalsoup)
pkgver=0.12.0
pkgrel=1
pkgdesc="A Python library for automating interaction with websites"
arch=('any')
url="https://github.com/hickford/MechanicalSoup"
license=('MIT')
makedepends=('python2-setuptools' 'python-setuptools')
source=("https://github.com/hickford/MechanicalSoup/archive/v${pkgver}.tar.gz")

check() {
  cd $srcdir/MechanicalSoup-$pkgver 
  python3 setup.py check
}

package_python2-mechanicalsoup() {
  depends=('python2' 'python2-beautifulsoup4' 'python2-requests' 'python2-six' 'python2-lxml')
  cd $srcdir/MechanicalSoup-$pkgver 

  python2 setup.py install --root="$pkgdir/" --optimize=1
}

package_python-mechanicalsoup() {
  depends=('python' 'python-beautifulsoup4' 'python-requests' 'python-six' 'python-lxml')
  cd $srcdir/MechanicalSoup-$pkgver 

  python setup.py install --root="$pkgdir/" --optimize=1
}

sha512sums=('dcbbe50d59b1314ea6c8ee17a5fa9b2dafc50b2a73f015de191a08d6c1ea367be329d9e9822e4da97f38fb7a5907d0a7ee5e24b43421bd14dae9950d6fed9cbd')
