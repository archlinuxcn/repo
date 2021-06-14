# Maintainer: Colin Arnott <colin@urandom.co.uk>
# Contributer: Jonathan Arnold <jdarnold@archlinux.us>
# Contributor: Zhang Hai <dreaming.in.code.zh@gmail.com>

pkgname=python-mechanicalsoup
pkgver=1.1.0
pkgrel=1
pkgdesc="A Python library for automating interaction with websites"
arch=('any')
url="https://github.com/hickford/MechanicalSoup"
license=('MIT')
makedepends=('python-setuptools')
source=("https://github.com/hickford/MechanicalSoup/archive/v${pkgver}.tar.gz")

check() {
  cd $srcdir/MechanicalSoup-$pkgver 
  python3 setup.py check
}

package() {
  depends=('python' 'python-beautifulsoup4' 'python-requests' 'python-six' 'python-lxml')
  cd $srcdir/MechanicalSoup-$pkgver 

  python setup.py install --root="$pkgdir/" --optimize=1
}

sha512sums=('57f4120f9d6e0e5435d3d20330678fa9dc80215bd8a8009e7873c48b208b28ebe930baacb420f29a7caddd8df7d8e87c6452ba2b26514c6b5d386a1f1df46ae8')
