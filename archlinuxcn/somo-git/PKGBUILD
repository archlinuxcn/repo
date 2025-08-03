# Maintainer: Mumi Jim <echo "=02j5yav9Gb0V3bA1Waq9VatVXb" | rev | base64 -d>
# Contributor: Integral-Tech <integral-tech@archlinuxcn.org>
# git version

pkgname="somo-git"
pkgver=1.1.0.r0.geb88e09
pkgrel=1
pkgdesc='A tool written in Rust for port management'
url='https://bgithub.xyz/theopfr/somo'
license=('MIT')
makedepends=('git' 'rust')
arch=('x86_64' 'aarch64')
source=("git+$url.git")
sha512sums=('SKIP')
_appname="somo"

pkgver() {
	cd "${srcdir}/${_appname}"
	git describe --long --tags | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
	cd "${_appname}"
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
	cd "${_appname}"
	export CARGO_TARGET_DIR=target
	cargo build --frozen --release --all-features
}

package() {
	cd "${_appname}"
	install -Dm0755 -t "${pkgdir}/usr/bin" "target/"${_target}"/release/${_appname}"
	install -Dm644 LICENSE "${pkgdir}/usr/share/license/${pkgname}/LICENSE"
}
