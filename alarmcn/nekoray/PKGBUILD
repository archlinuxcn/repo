# Maintainer: Chi_Tang <me@chitang.dev>
# Maintainer: Integral <integral@member.fsf.org>

pkgname=nekoray
pkgver=4.3.7
_pkgver=${pkgver/.beta/-beta}
pkgrel=1
pkgdesc="Qt based cross-platform GUI proxy configuration manager (backend: sing-box)"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/Mahdi-zarei/${pkgname}"
license=('GPL-3.0-or-later')
makedepends=('cmake' 'go' 'qt6-tools')
depends=('qt6-base' 'qt6-charts' 'protobuf' 'yaml-cpp' 'zxing-cpp' 'abseil-cpp' 'cpr')
optdepends=(
	'sing-geoip-db: geoip database for NekoBox'
	'sing-geosite-db: geosite database for NekoBox'
)
source=(
	"${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/${_pkgver}.tar.gz"
	${pkgname}.{sh,desktop}
)
install="${pkgname}.install"
sha512sums=('d9a4d87d0dd3d5c10626c44664349b8eb3e76498a9efe2bc1e97005fee7d9556594a2653acba3609135eda175c3a38398fc8cdf0c2f56007dc5de1c8df76bea6'
            'b377f7e8c859ee0b5bc05f89e2dc6c0b8535e740e089e9afe5e5f145c38a05fccbbddfcb6eb8ced9a7478e4d9ccc3cbd3ffb6843c128189c75599c40c87737e8'
            'b0cfd99d7fd038d660af275a5f2fc7f9ebfe63d6751edd6eea66a8c5350f314b6dbc9eddaa5aaed134e97087290630d369b1bdf4ad59d12868c780103b33dbed')

build() {
	cd "${pkgname}-${pkgver}/"

	cmake -B build \
		-DCMAKE_BUILD_TYPE=None \
		-DCMAKE_INSTALL_PREFIX=/usr

	cmake --build build

	export CGO_CPPFLAGS="${CPPFLAGS}"
	export CGO_CFLAGS="${CFLAGS}"
	export CGO_CXXFLAGS="${CXXFLAGS}"
	export CGO_LDFLAGS="${LDFLAGS}"

	cd core/server
	VERSION_SINGBOX=$(go list -m -f '{{.Version}}' github.com/sagernet/sing-box)
	go build -o ../../build/ \
		-buildmode=pie \
		-trimpath \
		-ldflags "-linkmode=external -w -s -X 'github.com/sagernet/sing-box/constant.Version=${VERSION_SINGBOX}'" \
		-mod=readonly \
		-modcacherw \
		-tags "with_clash_api,with_gvisor,with_quic,with_wireguard,with_utls,with_ech,with_dhcp"
}

package() {
	install -Dm644 "${pkgname}.desktop" -t "${pkgdir}/usr/share/applications/"
	install -Dm755 "${pkgname}.sh" "${pkgdir}/usr/bin/${pkgname}"

	cd "${pkgname}-${pkgver}/"
	install -Dm644 "res/public/nekobox.png" -t "${pkgdir}/usr/share/pixmaps/"
	install -Dm755 build/{${pkgname},nekobox_core} -t "${pkgdir}/usr/lib/${pkgname}/"
}
