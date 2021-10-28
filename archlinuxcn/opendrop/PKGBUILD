# Maintainer: Konstantin Shalygin <k0ste@k0ste.ru>
# Contributor: Konstantin Shalygin <k0ste@k0ste.ru>

pkgname='opendrop'
pkgver='0.13.0'
pkgrel='1'
pkgdesc='An open Apple AirDrop implementation'
arch=('any')
url="https://github.com/seemoo-lab/${pkgname}"
license=('GPL')
depends=('python-requests' 'python-fleep' 'python-ifaddr'
	 'python-pillow' 'python-requests-toolbelt'
	 'python-ctypescrypto' 'python-libarchive-c'
	 'python-netifaces'
	 'python-zeroconf' 'owlink')
makedepends=('python' 'python-setuptools')
source=("${url}/archive/v${pkgver}.tar.gz")
sha256sums=('1684ee1497615b6d9c410d73f0712ebc2b6b5c706075e75fb6799175264e4de5')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  python setup.py install -O1 --skip-build --root="${pkgdir}"
}
