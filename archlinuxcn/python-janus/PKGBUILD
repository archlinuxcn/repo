# Maintainer: Bruce Zhang <zttt183525594@gmail.com>
pkgname=python-janus
_name=${pkgname#python-}
pkgver=0.5.0
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
sha256sums=('0700f5537d076521851d19b7625545c5e76f6d5792ab17984f28230adcc3b34c')

build() {
	cd "$_name-$pkgver"
	LANG=en_US.UTF-8 python setup.py build
}

package() {
	cd "$_name-$pkgver"
	LANG=en_US.UTF-8 python setup.py install --root="$pkgdir/" --optimize=1 --skip-build
}
