# Maintainer: Rhinoceros <https://aur.archlinux.org/account/rhinoceros>
# Contributor: Abhishek Mudgal
# Contributor: Ivan Semkin (ivan at semkin dot ru)

_pkgname=vdf
pkgname=python-vdf
pkgver=3.5
pkgrel=1
pkgdesc="Library for working with Valve's VDF text format"
arch=('any')
url='https://github.com/solsticegamestudios/vdf'
license=('MIT')
depends=('python>=3.3')
# if python < 3.3, will need python-mock as checkdepends https://mock.readthedocs.io/en/latest/
makedepends=(python-setuptools)
checkdepends=(python-nose python-coverage)
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('79768533023f9fd08d329924947912408ce65a97680e44422cbe2aff0d1594bb')

build() {
  cd "$_pkgname-$pkgver"
  python setup.py build
}

check() {
  cd "$_pkgname-$pkgver"
  python setup.py test
}

package() {
  cd "$_pkgname-$pkgver"
  python setup.py install --optimize=1 --root="${pkgdir}/"
  install -D -m644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
