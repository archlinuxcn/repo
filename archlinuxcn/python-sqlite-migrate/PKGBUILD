# Maintainer: Cameron Otsuka <cameron@otsuka.haus>
# Contributor: Cameron Otsuka <cameron@otsuka.haus>
pkgname="python-sqlite-migrate"
_name=${pkgname#python-}
pkgver="0.1b0"
pkgrel=3
pkgdesc="A simple database migration system for SQLite, based on sqlite-utils"
arch=("any")
url="https://github.com/simonw/sqlite-migrate"
license=("Apache-2.0")
depends=("python" "python-click" "sqlite-utils")
makedepends=("python-build" "python-installer" "python-poetry" "python-setuptools" "python-wheel")
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/simonw/sqlite-migrate/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=("SKIP")

build() {
	cd "${_name}-${pkgver}"
	python -m build --wheel --no-isolation
}

package() {
	cd "${_name}-${pkgver}"
	python -m installer --destdir="$pkgdir" dist/*.whl
}
