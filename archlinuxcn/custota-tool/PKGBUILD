# Maintainer: Integral <integral@member.fsf.org>

pkgname=custota-tool
_srcname=Custota
pkgver=5.15
pkgrel=1
pkgdesc="Android A/B OTA updater app for custom OTA servers"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/chenxiaolong/${_srcname}"
license=('GPL-3.0-or-later')
makedepends=('cargo')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('15f5ab785a87839f266a4fe630f1cf507e6d848b311d3a9bdb3f6710504d91ff')

prepare() {
	cd "${_srcname}-${pkgver}/${pkgname}/"
	cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
	cd "${_srcname}-${pkgver}/${pkgname}/"
	cargo build --frozen --release --all-features
}

package() {
	cd "${_srcname}-${pkgver}/${pkgname}/"
	install -Dm755 "target/release/${pkgname}" -t "${pkgdir}/usr/bin/"
}
