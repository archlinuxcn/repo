# Maintainer: Integral <integral@member.fsf.org>
# Maintainer: cubercsl <2014cais01 at gmail dot com>

pkgname=dae
pkgver=1.1.0rc1
pkgrel=1
pkgdesc="A Linux lightweight and high-performance transparent proxy solution based on eBPF."
arch=('x86_64' 'aarch64')
url="https://github.com/daeuniverse/${pkgname}"
license=('AGPL-3.0-or-later')
depends=(
	'glibc'
	'v2ray-geoip'
	'v2ray-domain-list-community'
)
makedepends=('clang' 'go')
backup=("etc/${pkgname}/config.${pkgname}")
source=("${pkgname}-${pkgver}.tar.xz::${url}/releases/download/v${pkgver}/${pkgname}-full-src.tar.xz")
install="${pkgname}.install"
sha256sums=('62ceafadd4b3634e01456e0badc6fda2a4c920495a6a7805d66a1f19d88b86fe')

build() {
	export CFLAGS="-fno-stack-protector"
	export CGO_ENABLED=1
	export CGO_CPPFLAGS="${CPPFLAGS}"
	export CGO_CFLAGS="${CFLAGS}"
	export CGO_CXXFLAGS="${CXXFLAGS}"
	export CGO_LDFLAGS="${LDFLAGS}"
	export BUILD_ARGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
	make VERSION="${pkgver}"
}

package() {
	install -Dm755 "${pkgname}" -t "${pkgdir}/usr/bin/"
	install -Dm644 "install/${pkgname}.service" -t "${pkgdir}/usr/lib/systemd/system/"
	install -Dm640 "install/empty.${pkgname}" "${pkgdir}/etc/${pkgname}/config.${pkgname}"
	install -Dm644 "example.${pkgname}" "${pkgdir}/etc/${pkgname}/config.${pkgname}.example"

	mkdir -p "${pkgdir}/usr/share/${pkgname}/"
	ln -vs /usr/share/v2ray/geoip.dat "${pkgdir}/usr/share/${pkgname}/geoip.dat"
	ln -vs /usr/share/v2ray/geosite.dat "${pkgdir}/usr/share/${pkgname}/geosite.dat"
}
