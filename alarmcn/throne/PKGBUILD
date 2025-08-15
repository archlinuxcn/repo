# Maintainer: Chi_Tang <me@chitang.dev>
# Maintainer: Integral <integral@member.fsf.org>

pkgname=throne
_srcname=Throne
pkgver=1.0.1
pkgrel=4
pkgdesc="Qt based cross-platform GUI proxy configuration manager (backend: sing-box)"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/throneproj/${pkgname}"
license=('GPL-3.0-or-later')
depends=('qt6-base' 'qt6-charts')
makedepends=('cmake' 'go' 'qt6-tools' 'protobuf' 'vulkan-headers')
optdepends=(
	'sing-geoip-db: geoip database for Throne'
	'sing-geosite-db: geosite database for Throne'
)
conflicts=('nekoray')
replaces=('nekoray')
source=(
	"${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/${pkgver}.tar.gz"
	"${pkgname}.sh"
	"${_srcname}.desktop"
)
sha512sums=('686ea789611294bc0c6fd668d4a6c5e3d4511f24550df5da3ae85dd24432c7e87792388778bd5c0690aad6f74c1e84c0d256cc77cd39e5c5695e3827cc6a0248'
            '28275441d2d1eb3203d3d4084666d5f8f8af03e29feee97fb758f6ba87396a45876221316e11aab1a159ef8a67fe8d62d75ff8d38131cb3dca3221bb1d98085c'
            'a47e8b547bd8759e7bc5c31f6055ad5ed3f6ee5879c07de8c05349b381578f907d3bdfb833fd5296fb4b20b6cacae6b622b2ab1fc7e46fce309cb273e82bc1c5')

prepare() {
	cd "${_srcname}-${pkgver}/core/server"
	export GOBIN="${srcdir}/bin"
	export PATH="${PATH}:${GOBIN}"
	go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
	go install github.com/chai2010/protorpc/protoc-gen-protorpc@latest

	cd gen
	protoc -I . --go_out=. --protorpc_out=. libcore.proto
}

build() {
	cd "${_srcname}-${pkgver}/"

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
		-tags "with_clash_api,with_gvisor,with_quic,with_wireguard,with_utls,with_dhcp,with_tailscale"
}

package() {
	install -Dm644 "${_srcname}.desktop" -t "${pkgdir}/usr/share/applications/"
	install -Dm755 "${pkgname}.sh" "${pkgdir}/usr/bin/${pkgname}"

	cd "${_srcname}-${pkgver}/"
	install -Dm644 "res/public/${_srcname}.png" -t "${pkgdir}/usr/share/pixmaps/"
	install -Dm755 build/{Core,Throne} -t "${pkgdir}/usr/lib/${pkgname}/"
}
