# Maintainer: Integral <integral@archlinuxcn.org>

pkgname=flymd
pkgver=0.8.3
pkgrel=1
pkgdesc="A 7MB high-performance Markdown note tool"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/flyhunterl/${pkgname}"
license=('GPL-3.0-only')
depends=('cairo' 'gcc-libs' 'gdk-pixbuf2' 'glib2' 'gtk3' 'libsoup3' 'webkit2gtk-4.1')
makedepends=('npm' 'cargo')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('6f07aea6edcf8895b8608351cf5e684a8d0a07f4d3759ff37d75591d89acfe82')

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
