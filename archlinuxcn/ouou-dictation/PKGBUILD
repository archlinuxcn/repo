# Maintainer: Integral <integral@member.fsf.org>

pkgname=ouou-dictation
pkgver=1.0.0
pkgrel=3
pkgdesc="A command-line program for self-help dictation supporting Chinese, Japanese and English"
arch=('x86_64' 'aarch64')
url="https://github.com/OuOu2021/${pkgname}"
license=('Apache-2.0 OR MIT')
depends=('speech-dispatcher')
makedepends=('cargo' 'clang' 'libspeechd')
optdepends=('festival: Speech output using Festival'
	'espeak-ng: Speech output using ESpeak-ng')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('b64abb8684adbcddf698bbfe3cfa5267e257228f34493ffe42a5d95698d3ff91')

prepare() {
	cd "${pkgname}-${pkgver}/"
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
	cd "${pkgname}-${pkgver}/"
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	cargo build --frozen --release --all-features
}

package() {
	cd "${pkgname}-${pkgver}/"
	install -Dm755 "target/release/${pkgname/-/_}" "${pkgdir}/usr/bin/${pkgname}"
	install -Dm644 LICENSE-{APACHE,MIT} -t "${pkgdir}/usr/share/licenses/${pkgname}/"
}
