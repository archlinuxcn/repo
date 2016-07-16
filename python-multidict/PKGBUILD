# Maintainer: renek <aur@spaceshore.net>
_pkgname=multidict
pkgname=python-${_pkgname}
pkgver=1.1.0b4
pkgrel=1
pkgdesc="A multidict implementation"
arch=('any')
url='https://github.com/aio-libs/multidict'
license=('APACHE')
depends=('python')
makedepends=('cython' 'python-setuptools')
source=("https://github.com/aio-libs/multidict/archive/v${pkgver}.tar.gz")
sha512sums=('b271f0be4cdf164aff59903dbf89689c18475731e146da1bb340c2307f0ee8d1fcf330de97e2300efc50df14c233ec5b74542b3e600017df1990a8e136dc3ae3')

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}/" --optimize=1
}
