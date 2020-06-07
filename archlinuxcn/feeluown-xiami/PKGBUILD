# Maintainer: Bruce Zhang <zttt183525594@gmail.com>
_name=fuo_xiami
pkgname=feeluown-xiami
pkgver=0.2.3
pkgrel=1
pkgdesc="feeluown xiami plugin"
arch=('any')
url="https://github.com/feeluown/feeluown-xiami"
license=('GPL3')
depends=('feeluown' 'python-marshmallow' 'python-requests')
makedepends=('python-setuptools' 'python-pip')
source=(
	"https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz"
)
sha256sums=('9467161e66dd8183424dfcd0752fbfb607e2efd92173805635e001181c1a6f14')
groups=('feeluown-full')

build() {
	cd "$_name-$pkgver"
	LANG=en_US.UTF-8 python setup.py build
}

package() {
	cd "$_name-$pkgver"
	LANG=en_US.UTF-8 python setup.py install --root="$pkgdir/" --optimize=1 --skip-build
}
