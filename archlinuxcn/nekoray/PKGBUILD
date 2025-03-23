# Maintainer: Chi_Tang <me@chitang.dev>
# Maintainer: Integral <integral@member.fsf.org>

pkgname=nekoray
pkgver=4.2.12
_pkgver=${pkgver/.beta/-beta}
pkgrel=1
pkgdesc="Qt based cross-platform GUI proxy configuration manager (backend: sing-box)"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://matsuridayo.github.io"
license=('GPL-3.0-or-later')
makedepends=('cmake' 'git' 'go')
depends=(
	'qt6-base' 'qt6-svg' 'qt6-tools'
	'protobuf' 'yaml-cpp' 'zxing-cpp'
	'abseil-cpp' 'cpr'
)
optdepends=(
	'sing-geoip: geoip data for NekoBox'
	'sing-geosite: geosite data for NekoBox'
)
source=(
	"git+https://github.com/Mahdi-zarei/${pkgname}.git#tag=${_pkgver}"
	${pkgname}.{sh,desktop}
)
sha512sums=('21ec6d5d5311bae60f657dfb472294c3cf1f3afb0529db0c13c43d1b521908a070f31cb2adbd8d0b39b53bbb6bff2bbfe023a099d9d619899580ed2a6de2828a'
            'e277cb5fcb5bbcc23b2748d63dd057bff33763407243bf30769bfa8f702e9859360a07bae9481142785683d490336574262bbc247ea37e5163cd112fe68f4075'
            'b0cfd99d7fd038d660af275a5f2fc7f9ebfe63d6751edd6eea66a8c5350f314b6dbc9eddaa5aaed134e97087290630d369b1bdf4ad59d12868c780103b33dbed')

build() {
	cd "${pkgname}/"

	cmake -B build \
		-DCMAKE_BUILD_TYPE=None \
		-DCMAKE_INSTALL_PREFIX=/usr

	cmake --build build

	export GOARCH

	case $CARCH in
	x86_64) GOARCH=amd64 ;;
	aarch64) GOARCH=arm64 ;;
	riscv64) GOARCH=riscv64 ;;
	esac

	GOOS=linux ./script/build_go.sh
}

package() {
	install -Dm644 "${pkgname}.desktop" -t "${pkgdir}/usr/share/applications/"
	install -Dm755 "${pkgname}.sh" "${pkgdir}/usr/bin/nekobox"

	cd "${pkgname}/"
	install -Dm644 "res/public/nekobox.png" -t "${pkgdir}/usr/share/pixmaps/"

	# Core
	local core_srcdir=linux

	case $CARCH in
	x86_64) core_srcdir+=64 ;;
	aarch64) core_srcdir+=-arm64 ;;
	riscv64) core_srcdir+=-riscv64 ;;
	esac

	install -Dm755 "deployment/${core_srcdir}/nekobox_core" -t "${pkgdir}/usr/lib/${pkgname}/"

	# Binary file
	install -Dm755 "build/${pkgname}" -t "${pkgdir}/usr/lib/${pkgname}/"
}
