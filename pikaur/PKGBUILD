# Maintainer: Yauheni Kirylau <actionless dot loveless AT gmail.com>
# shellcheck disable=SC2034,SC2154

pkgname=pikaur
pkgver=1.2.21
pkgrel=1
pkgdesc="AUR helper with minimal dependencies inspired by pacaur, yaourt and yay. Review PKGBUILDs all in once, next build them all without user interaction."
arch=('any')
url="https://github.com/actionless/pikaur"
license=('GPL3')
source=(
	"$pkgname-$pkgver.tar.gz"::https://github.com/actionless/pikaur/archive/"$pkgver".tar.gz
)
md5sums=('5b657db0496f857ad78b48fdffec4af8')
depends=(
	'pacman'
	'pyalpm'
	'git'
)
optdepends=(
	'asp: for ABS support in -G/--getpkgbuild operation'
)
conflicts=('pikaur-git')

build() {
	cd "${srcdir}/${pkgname}-${pkgver}" || exit 2
	sed -i -e "s/VERSION.*=.*/VERSION = '${pkgver}'/g" pikaur/config.py
	make
}

package() {
	cd "${srcdir}/${pkgname}-${pkgver}" || exit 2
	python setup.py install --prefix=/usr --root="$pkgdir/" --optimize=1
	for langmo in $(cd ./locale && ls ./*.mo); do
		lang=$(sed -e 's/.mo$//' <<< "${langmo}")
		install -Dm644 "locale/${langmo}" "$pkgdir/usr/share/locale/${lang}/LC_MESSAGES/pikaur.mo"
	done
	install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
	install -Dm644 pikaur.1 "$pkgdir/usr/share/man/man1/pikaur.1"
	cp -r ./packaging/* "${pkgdir}"
}
