# Contributor: Francois Boulogne <fboulogne at april dot org>
# Maintainer: Francois Boulogne <fboulogne at april dot org>

pkgname=python2-pypdf2
pkgver=1.25.1
pkgrel=1
pkgdesc="PDF toolkit"
arch=('any')
url="http://mstamy2.github.com/PyPDF2"
license=('BSD')
depends=('python2')
makedepends=('python2-setuptools')
source=(https://pypi.python.org/packages/source/P/PyPDF2/PyPDF2-$pkgver.tar.gz)

package(){
  cd "$srcdir/PyPDF2-$pkgver"
  python2 setup.py install --root="$pkgdir/" --optimize=1
  install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:ts=2:sw=2:et:
sha256sums=('43d324f70f8994c25a08e6edc02ec2d5c1e84c9231d3537f785b3f97641182eb')
