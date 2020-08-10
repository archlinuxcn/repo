# Maintainer: Bruce Zhang <zttt183525594@gmail.com>
_name=fuo_qqmusic
pkgname=feeluown-qqmusic
pkgver=0.3
pkgrel=1
pkgdesc="feeluown qqmusic plugin"
arch=('any')
url="https://github.com/feeluown/feeluown-qqmusic"
license=('GPL3')
depends=('feeluown' 'python-marshmallow' 'python-requests')
makedepends=('python-setuptools' 'python-pip')
source=(
	"https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz"
)
sha256sums=('0abb5bbadc2aa1d903b5f9652da04d40c426ad500d26e9ed98f0175966bb96dc')
groups=('feeluown-full')

build() {
	cd "$_name-$pkgver"
	LANG=en_US.UTF-8 python setup.py build
}

package() {
	cd "$_name-$pkgver"
	LANG=en_US.UTF-8 python setup.py install --root="$pkgdir/" --optimize=1 --skip-build
}
