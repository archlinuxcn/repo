# Maintainer: Shayne Hartford <shayneehartford@gmail.com>

pkgname=protondb-tags
_pkgname=ProtonDB-Tags
pkgver=1.1.0
pkgrel=1
pkgdesc="Pull ratings from ProtonDB and import them into your Steam library as tags."
arch=('any')
url="https://github.com/CorruptComputer/$_pkgname"
license=('MIT')
depends=(
    'python-vdf'
    'python-requests'
)
optdepends=(
    'steam: Supports any steam, native, flatpak, etc'
)
provides=('protondb-tags')
source=(https://github.com/CorruptComputer/$_pkgname/archive/$pkgver.zip)
md5sums=('64472d2a0795255100fe4e9164f31e12')

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  
  install -Dm755 $_pkgname.py "$pkgdir/usr/bin/$_pkgname"
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
