# Maintainer: Yauhen Kirylau <actionless DOT loveless PLUS aur AT gmail MF com>
# shellcheck disable=SC2001,SC2034,SC2154 shell=bash

_pkgname=pikaur
pkgname="${_pkgname}"
pkgver=1.33
pkgrel=1
pkgdesc="AUR helper which asks all questions before installing/building. Inspired by pacaur, yaourt and yay."
arch=('any')
url="https://github.com/actionless/pikaur"
license=('GPL-3.0-only')
source=(
	"$pkgname-$pkgver.tar.gz"::${url}/archive/"$pkgver".tar.gz
)
b2sums=('849c5fe720e570db7bfc26b256f8c077b1d14262b2378728e3c3bced22a69e456759a7c83f1265be7a2390849c9d836eb84fac88d144b068eab0a746fb7da356')
depends=(
	'pyalpm'
	'git'
)
makedepends=(
	'python-wheel'
	'python-hatchling'
	'python-build'
	'python-installer'
	'python-setuptools'  # i think it normally should be required by python-pep517 which required by python-build/installer
	'python-markdown-it-py'
)
optdepends=(
	'devtools: for Arch Pkgs support in -G/--getpkgbuild operation'
	'python-pysocks: for socks5 proxy support'
	'python-defusedxml: securely wrap Arch news replies'
	'pacman-contrib: to use in pacman hook/systemd timer for cleaning up pikaur cache'
)
conflicts=("${_pkgname}-git")
provides=("$_pkgname")
changelog="CHANGELOG"

build() {
	cd "${srcdir}/${pkgname}-${pkgver}" || exit 2
	sed -i -e "s/^VERSION[: ].*=.*/VERSION = '${pkgver}'/g" pikaur/config.py
	if test -d ./dist ; then
		rm -r ./dist
	fi
	make
	/usr/bin/python3 -m build --wheel --no-isolation
}

package() {
	cd "${srcdir}/${pkgname}-${pkgver}" || exit 2
	/usr/bin/python3 -m installer --destdir="$pkgdir" dist/*.whl
	for langmo in $(cd ./locale && ls ./*.mo); do
		lang=$(sed -e 's/.mo$//' <<< "${langmo}")
		install -Dm644 "locale/${langmo}" "$pkgdir/usr/share/locale/${lang}/LC_MESSAGES/pikaur.mo"
	done
	install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
	install -Dm644 pikaur.1 "${pkgdir}/usr/share/man/man1/${_pkgname}.1"
	cp -r ./packaging/* "${pkgdir}"
}
