# Maintainer: Timothée Girard <aur@timotheegirard.com>
# Contributor: Eduardo Sánchez Muñoz <eduardosanchezmunoz@gmail.com>

pkgname=htmlcxx
pkgver=0.87
pkgrel=1
pkgdesc="A simple non-validating CSS1 and HTML parser for C++."
arch=('i686' 'x86_64')
url="http://htmlcxx.sourceforge.net/"
license=('LGPL')
depends=()
makedepends=()
conflicts=('htmlcxx' 'libhtmlcxx' 'libcss_parser')
provides=('htmlcxx' 'libhtmlcxx' 'libcss_parser')
source=("https://sourceforge.net/projects/${pkgname}/files/v${pkgver}/${pkgname}-${pkgver}.tar.gz")
sha256sums=('5d38f938cf4df9a298a5346af27195fffabfef9f460fc2a02233cbcfa8fc75c8')

build() {
	cd "${srcdir}/${pkgname}-${pkgver}"

	LDFLAGS="$LDFLAGS -Wl,--no-as-needed"
	./configure --prefix=/usr
	make
}

package() {
	cd "${srcdir}/${pkgname}-${pkgver}"
	make DESTDIR="${pkgdir}" install
}
