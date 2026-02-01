# Maintainer: Jax Young <jaxvanyang@gmail.com>
# Maintainer: Murli Tawari <kraanzu@gmail.com>

pkgname=smassh
pkgver=3.2.1
pkgrel=2
pkgdesc="TUI based typing test application inspired by MonkeyType"
url="https://github.com/kraanzu/smassh"
arch=('any')
license=('GPL-3.0-only')
depends=(
        'python>=3.8.1'
        'python-textual>=0.81.0'
        'python-click>=8.1.7'
        'python-requests>=2.31.0'
        'python-platformdirs>=4.3.6'
        'python-rich'
)
makedepends=(
        'python-build'
        'python-installer'
        'python-wheel'
        'python-hatchling'
)
source=("$pkgname-$pkgver.tar.gz::${url}/archive/v$pkgver.tar.gz")
sha256sums=('29550e1dd204ccf93a9f314bbf7b8977a6a8b1f3fb33a808b43420ca935e8bc4')

build() {
        cd "$pkgname-$pkgver"
        python -m build --wheel --no-isolation
}

package() {
        cd "$pkgname-$pkgver"
        python -m installer --destdir "$pkgdir" dist/*.whl
}
