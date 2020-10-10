# Maintainer: Bruce Zhang <zttt183525594@gmail.com>
pkgname=python-janus
_name=${pkgname#python-}
pkgver=0.6.0
pkgrel=1
pkgdesc="Thread-safe asyncio-aware queue for Python"
arch=('any')
url="https://github.com/aio-libs/janus"
license=('Apache')
depends=('python')
makedepends=('python-setuptools')
checkdepends=('python-pytest')

source=(
	"https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz" 
)
sha256sums=('7bc6a9b99f401978113937f477b30ef5a104897e92f6f831aa5b95b57d103eb1')

build() {
	cd "$_name-$pkgver"
	LANG=en_US.UTF-8 python setup.py build
}

package() {
	cd "$_name-$pkgver"
	LANG=en_US.UTF-8 python setup.py install --root="$pkgdir/" --optimize=1 --skip-build
}
