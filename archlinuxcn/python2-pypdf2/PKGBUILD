# Contributor: Francois Boulogne <fboulogne at april dot org>
# Maintainer: Francois Boulogne <fboulogne at april dot org>

pkgname=python2-pypdf2
pkgver=1.26.0
pkgrel=1
pkgdesc="PDF toolkit"
arch=('any')
url="http://mstamy2.github.com/PyPDF2"
license=('BSD')
depends=('python2')
makedepends=('python2-setuptools')
source=(https://pypi.python.org/packages/b4/01/68fcc0d43daf4c6bdbc6b33cc3f77bda531c86b174cac56ef0ffdb96faab/PyPDF2-$pkgver.tar.gz)

package(){
  cd "$srcdir/PyPDF2-$pkgver"
  python2 setup.py install --root="$pkgdir/" --optimize=1
  install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:ts=2:sw=2:et:
sha256sums=('e28f902f2f0a1603ea95ebe21dff311ef09be3d0f0ef29a3e44a932729564385')
