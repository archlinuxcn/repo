pkgname=sqlite-utils
pkgver=3.39
pkgrel=1
pkgdesc="CLI tool and Python utility functions for manipulating SQLite databases"
arch=("any")
url="https://sqlite-utils.datasette.io/"
license=("Apache")
depends=("python-sqlite-fts4" "python-click" "python-click-default-group" "python-tabulate" "python-dateutil" "python-pluggy")
makedepends=("python-build" "python-installer" "python-setuptools")
checkdepends=("python-pytest" "python-hypothesis")
conflicts=("sqlite-utils")
source=("https://pypi.io/packages/source/${pkgname::1}/${pkgname}/sqlite_utils-${pkgver}.tar.gz")
sha256sums=("bfa2eac29b3e3eb5c9647283797527febcf4efd4a9bbb31d979a14a11ef9dbcd")

build() {
	cd "sqlite_utils-${pkgver}"
	python -m build --wheel --no-isolation
}

check() {
	cd "sqlite_utils-${pkgver}"
	pytest
}

package() {
	cd "sqlite_utils-${pkgver}"
	python -m installer --destdir="$pkgdir" dist/*.whl
	install -Dm 644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
