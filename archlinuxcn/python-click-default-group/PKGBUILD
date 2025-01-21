# Maintainer: Felix Yan <felixonmars@archlinux.org>

pkgname=python-click-default-group
pkgver=1.2.4
pkgrel=3
pkgdesc="Extends click.Group to invoke a command without explicit subcommand name"
url="https://github.com/click-contrib/click-default-group"
license=('BSD-3-Clause')
arch=('any')
depends=('python-click')
makedepends=('python-build' 'python-installer' 'python-flit-core')
checkdepends=('python-pytest')
source=("https://github.com/click-contrib/click-default-group/archive/v$pkgver/$pkgname-$pkgver.tar.gz")
sha512sums=('0239e703421e693399e8e54e4a6bdc4a74e6f16307f008ee742788ce3e8040f633de2b1bf12997a5c448b70cb55f77ccd4f42c5b4abe3b6a05df18908daf61da')

build() {
  cd click-default-group-$pkgver
  python -m build -nw
}

check() {
  cd click-default-group-$pkgver
  python -m pytest
}

package() {
  cd click-default-group-$pkgver
  python -m installer -d "$pkgdir" dist/*.whl
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname/
}
