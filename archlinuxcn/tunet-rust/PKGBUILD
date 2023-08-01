# Maintainer: Integral <integral@murena.io>

pkgname=tunet-rust
pkgver=0.9.1
pkgrel=1
pkgdesc="A Tsinghua University network authentication client for Linux, written in Rust. 清华大学校园网 Rust 客户端"
url="https://github.com/Berrysoft/tunet-rust"
arch=('x86_64' 'aarch64')
license=('MIT')
depends=('openssl' 'freetype2' 'hicolor-icon-theme')
makedepends=('cargo')
source=(${pkgname}-${pkgver}.tar.gz::"https://github.com/Berrysoft/${pkgname}/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('b0242b86e797c498e29d73023c063b710eb2f70d218327747226d05f0e09f17888880cf424930699ef10826653669cd85d37b0d928fe154e28346bfa60e5c284')

build() {
	cd "${pkgname}-${pkgver}/"
	cargo build --release --workspace --exclude native
}

package() {
	cd "${pkgname}-${pkgver}/"

	# Binaries
	pushd "target/release/"
	for bin in tunet tunet-gui tunet-cui tunet-service; do
		install -Dm755 "${bin}" -t "${pkgdir}/usr/bin/"
	done

	popd
	# Desktop file
	install -Dm644 "tunet/tunet.desktop" -t "${pkgdir}/usr/share/applications/"

	# Icon
	install -Dm644 "logo.png" "${pkgdir}/usr/share/icons/hicolor/256x256/apps/tunet.png"

	# Service
	install -Dm644 "tunet-service/tunet@.service" -t "${pkgdir}/usr/lib/systemd/system/"

	# License
	install -Dm644 "LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}/"
}
