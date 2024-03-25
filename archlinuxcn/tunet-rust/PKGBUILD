# Maintainer: Integral <integral@member.fsf.org>

pkgname=tunet-rust
pkgver=0.9.3
pkgrel=1
pkgdesc="A Tsinghua University network authentication client for Linux, written in Rust. 清华大学校园网 Rust 客户端"
url="https://github.com/Berrysoft/tunet-rust"
arch=('x86_64' 'aarch64')
license=('MIT')
depends=('openssl' 'freetype2' 'hicolor-icon-theme')
makedepends=('cargo')
source=(${pkgname}-${pkgver}.tar.gz::"https://github.com/Berrysoft/${pkgname}/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('b19ed9f998a9e0a1ef9350efac3047f9828b2905b947540dfbb8c49731a6569498ccca9aa3ba890b27430fea519b297c20ec6df7dd0fd54cee6ea9f0b80e39eb')

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
