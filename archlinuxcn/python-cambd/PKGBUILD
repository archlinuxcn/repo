# Maintainer: Molyuu <mi@molyuu.cyou>
pkgname=python-cambd
_name=${pkgname#python-}
pkgver=1.0.2
pkgrel=1
pkgdesc="Cambridge dictionary cli app"
arch=('any')
url="https://github.com/rocktimsaikia/cambd"
license=('MIT')
groups=()
depends=('python' 'python-beautifulsoup4' 'python-html5lib' 'python-click' 'python-halo' 'python-requests' 'python-rich' 'python-simple-term-menu')
makedepends=('python-setuptools' 'python-pip')
provides=()
conflicts=()
replaces=()
backup=()
options=(!emptydirs)
install=
source=("https://github.com/rocktimsaikia/cambd/archive/refs/tags/v${pkgver}.zip")
sha256sums=('8bf444780e68f6c93358b25f22a3d9c1acd62c870a950077e1b6349729d72902')

build() {
    cd "$_name-$pkgver"
    python setup.py build
}

package() {
    cd "$_name-$pkgver"
    python setup.py install --root="$pkgdir" --optimize=1 --skip-build
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE.txt"
}
