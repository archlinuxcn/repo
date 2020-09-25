# Maintainer: Bruce Zhang <zttt183525594@gmail.com>
_name=fuo_qqmusic
pkgname=feeluown-qqmusic
pkgver=0.3.1
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
sha256sums=('1ee5a01fc684d08fcc43e0968e1b38477b24b7d5a0bbefcdd843970e9850701a')
groups=('feeluown-full')

build() {
	cd "$_name-$pkgver"
	LANG=en_US.UTF-8 python setup.py build
}

package() {
	cd "$_name-$pkgver"
	LANG=en_US.UTF-8 python setup.py install --root="$pkgdir/" --optimize=1 --skip-build
}
