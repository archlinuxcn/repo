# Maintainer: Yuanji <self@gimo.me>
# Contributor: Antonio Rojas <arojas@archlinux.org>
# Contributor: Francois Boulogne <fboulogne at april dot org>

pkgname=python-pypdf2
pkgver=1.26.0
pkgrel=2
pkgdesc='A utility to read and write PDFs with Python'
arch=(any)
url='https://mstamy2.github.com/PyPDF2'
license=(BSD)
depends=(python)
makedepends=(python-setuptools)
source=($pkgname-$pkgver.tar.gz::"https://github.com/mstamy2/PyPDF2/archive/$pkgver.tar.gz")
sha256sums=('140b1fed792f487f2fd814eb0e832a5b6ef5ae362da302c1fc5a9786d5acb469')

build() {
  cd PyPDF2-$pkgver
  python setup.py build
}

package(){
  cd PyPDF2-$pkgver
  python setup.py install --root="$pkgdir" --optimize=1
  install -D -m755 Scripts/pdfcat "$pkgdir"/usr/bin/pdfcat
  install -D -m644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
