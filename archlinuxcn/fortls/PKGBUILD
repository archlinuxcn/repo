# Maintainer: Colin Woodbury <colin@fosskers.ca>

pkgname=fortls
pkgver=2.13.0
pkgrel=4
pkgdesc="A modern Language Server for Fortran."
arch=(any)
url="https://github.com/gnikit/fortls"
license=("MIT")
depends=("python-json5"
		 "python-setuptools")
makedepends=("python-packaging"
			 "python-setuptools-scm")
provides=("fortran-language-server")
conflicts=("fortran-language-server")
source=("https://pypi.io/packages/source/f/${pkgname}/${pkgname}-${pkgver}.tar.gz")
sha256sums=('23c5013e8dd8e1d65bf07be610d0827bc48aa7331a7a7ce13612d4c646d0db31')

build() {
	cd "$pkgname-$pkgver"
	python setup.py build
}

package() {
	cd "$pkgname-$pkgver"
	python setup.py install --root="$pkgdir/" --optimize=1 --skip-build

	# License
	install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
