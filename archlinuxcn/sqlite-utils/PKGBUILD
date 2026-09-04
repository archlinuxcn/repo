pkgname=sqlite-utils
pkgver=4.2.1
pkgrel=1
pkgdesc="CLI tool and Python utility functions for manipulating SQLite databases"
arch=("any")
url="https://sqlite-utils.datasette.io/"
license=("Apache-2.0")
depends=("python-sqlite-fts4" "python-click>=8.3.1" "python-click-default-group>=1.2.3" "python-tabulate" "python-dateutil" "python-pluggy" "python-pip")
makedepends=("python-build" "python-installer" "python-setuptools")
checkdepends=("python-pytest" "python-hypothesis")
conflicts=("sqlite-utils")
source=("https://pypi.io/packages/source/${pkgname::1}/${pkgname}/sqlite_utils-${pkgver}.tar.gz")
sha256sums=('76114b6a5414714e6c70e5fa5c4781b301b590f6951b5da39c8cc60c21382ba1')

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
