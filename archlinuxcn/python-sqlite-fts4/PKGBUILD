# Maintainer: Cameron Otsuka <cameron@otsuka.haus>
# Contributor: Cameron Otsuka <cameron@otsuka.haus>
# Contributor: NBonaparte <nbonaparte at protonmail.com>
pkgname="python-sqlite-fts4"
_name=${pkgname#python-}
pkgver="1.0.3"
pkgrel=2
pkgdesc="Custom Python functions for working with SQLite FTS4"
arch=("any")
url="https://github.com/simonw/sqlite-fts4"
license=("Apache-2.0")
depends=("python")
makedepends=("python-build" "python-installer" "python-setuptools" "python-wheel")
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/simonw/sqlite-fts4/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=("SKIP")

build() {
    cd "${_name}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${_name}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
}
