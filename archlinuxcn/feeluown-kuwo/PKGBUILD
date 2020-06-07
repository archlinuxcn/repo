# Maintainer: Bruce Zhang <zttt183525594@gmail.com>
_name=fuo_kuwo
pkgname=feeluown-kuwo
pkgver=0.1.1
pkgrel=5
pkgdesc="Kuwo music provider for FeelUOwn music player"
arch=('any')
url="https://github.com/feeluown/feeluown-kuwo"
license=('GPL3')
depends=('feeluown' 'python-marshmallow' 'python-requests')
makedepends=('python-setuptools' 'python-pip')
source=(
	"https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz"
)
sha256sums=('d34902a43b3f381ec969ef1127883960736f535bd6233b7984c86d0af684f948')
groups=('feeluown-full')

build() {
	cd "$_name-$pkgver"
	LANG=en_US.UTF-8 python setup.py build
}

package() {
	cd "$_name-$pkgver"
	LANG=en_US.UTF-8 python setup.py install --root="$pkgdir/" --optimize=1 --skip-build
}
