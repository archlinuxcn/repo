# Maintainer: Integral <integral@member.fsf.org>

pkgname=tunet-rust
pkgver=0.9.4
pkgrel=1
pkgdesc="A Tsinghua University network authentication client for Linux, written in Rust. 清华大学校园网 Rust 客户端"
url="https://github.com/Berrysoft/tunet-rust"
arch=('x86_64' 'aarch64')
license=('MIT')
depends=('openssl' 'freetype2' 'hicolor-icon-theme')
makedepends=('cargo')
source=(${pkgname}-${pkgver}.tar.gz::"https://github.com/Berrysoft/${pkgname}/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('79c50069ea0c484c369bc7aea1cb79d0fd77e2f1bf5c2bd87ac7e5ace4c6ca469acd438ac24403a1c4cd97cc051d250f40c457a74dd23a3b9bdd6846f0b6bb81')

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
