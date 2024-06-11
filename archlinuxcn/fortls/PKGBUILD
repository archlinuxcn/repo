# Maintainer: Colin Woodbury <colin@fosskers.ca>

pkgname=fortls
pkgver=3.1.1
pkgrel=1
pkgdesc="A modern Language Server for Fortran."
arch=(any)
url="https://github.com/gnikit/fortls"
license=("MIT")
depends=("python-json5")
makedepends=("python-build" "python-installer" "python-wheel" "python-setuptools-scm")
provides=("fortran-language-server")
conflicts=("fortran-language-server")
source=("https://pypi.io/packages/source/f/${pkgname}/${pkgname}-${pkgver}.tar.gz")
sha256sums=('ef248ce72bd1656d37ddb4d52f67c4764926102c749fc65b58429dcf9120e48d')

build() {
	cd "$pkgname-$pkgver"
    python -m build --wheel --no-isolation
}

package() {
	cd "$pkgname-$pkgver"
    python -m installer --destdir="$pkgdir" dist/*.whl

	# License
	install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
