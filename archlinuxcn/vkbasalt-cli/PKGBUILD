# Maintainer: Fabio 'Lolix' Loli <fabio.loli@disroot.org> -> https://github.com/FabioLolix

pkgname=vkbasalt-cli
pkgver=3.1.1
pkgrel=2
pkgdesc="Command-line utility for vkBasalt"
arch=(any)
url="https://gitlab.com/TheEvilSkeleton/vkbasalt-cli"
license=(LGPL3)
depends=(python)
makedepends=(git python-build python-wheel python-installer python-setuptools)
source=("git+https://gitlab.com/TheEvilSkeleton/vkbasalt-cli.git#tag=v${pkgver}")
sha256sums=('SKIP')

build() {
  cd vkbasalt-cli
  python -m build --wheel --no-isolation
}

package() {
  cd vkbasalt-cli
  python -m installer --destdir="$pkgdir" dist/*.whl
}