# Maintainer: Bruce Zhang <zttt183525594@gmail.com>
_name=fuo_netease
pkgname=feeluown-netease
pkgver=0.4.3
pkgrel=1
pkgdesc="feeluown netease plugin"
arch=('any')
url="https://github.com/feeluown/feeluown-netease"
license=('GPL3')
depends=('feeluown' 'python-pycryptodome' 'python-requests' 'python-marshmallow' 'python-beautifulsoup4')
makedepends=('python-setuptools' 'python-pip')
source=(
	"https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz"
)
sha256sums=('20aaa240f034a53a948e2f9d2ff9ec953cb6a98052245a6b6c1912ef6cecf38e')
groups=('feeluown-full')

build() {
	cd "$_name-$pkgver"
	LANG=en_US.UTF-8 python setup.py build
}

package() {
	cd "$_name-$pkgver"
	LANG=en_US.UTF-8 python setup.py install --root="$pkgdir/" --optimize=1 --skip-build
}
