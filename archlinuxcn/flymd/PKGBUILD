# Maintainer: Integral <integral@archlinuxcn.org>

pkgname=flymd
pkgver=1.3.0
pkgrel=1
pkgdesc="A 7MB high-performance Markdown note tool"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/flyhunterl/${pkgname}"
license=('GPL-3.0-only')
depends=('cairo' 'gcc-libs' 'gdk-pixbuf2' 'glib2' 'gtk3' 'libsoup3' 'webkit2gtk-4.1')
makedepends=('npm' 'cargo')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('df156f69479fafc7ab658e4c9d06658868a19931d18b9ddd95543b8da3366706')

prepare() {
	cd "${pkgname}-${pkgver}/"
	npm ci

	cd src-tauri
	cargo fetch --locked --target $(rustc --print host-tuple)
}

build() {
	cd "${pkgname}-${pkgver}/"
	CFLAGS+=" -ffat-lto-objects" npm run tauri:build -- --bundles deb
}

package() {
	case "${CARCH}" in
	"x86_64") local _debarch="amd64" ;;
	"aarch64") local _debarch="arm64" ;;
	"riscv64") local _debarch="riscv64" ;;
	esac

	cp -a ${pkgname}-${pkgver}/src-tauri/target/release/bundle/deb/${pkgname}_${pkgver}_${_debarch}/data/* "${pkgdir}"
}
