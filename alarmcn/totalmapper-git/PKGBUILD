# Maintainer: Hoream <hoream@qq.com>
_pkgname="totalmapper"
pkgname="${_pkgname}-git"
pkgver=1.4.8.r3.g59dafb8
pkgrel=2
pkgdesc="A simple utility for remapping keys using the Linux event handling system."
arch=(x86_64 aarch64)
url="https://github.com/ellbur/totalmapper"
license=('GPL3')
depends=()
provides=("${_pkgname}")
conflicts=("${_pkgname}" "${_pkgname}-bin")
makedepends=('cargo' 'git' 'glibc' 'gcc-libs')
source=("${_pkgname}::git+${url}")
sha512sums=('SKIP')

pkgver() {
	cd "${srcdir}/${_pkgname}"
	git describe --tags | sed -E 's/([^-]*-g)/r\1/;s/-/./g;s/^v//'
}

build() {
	cd "${srcdir}/${_pkgname}"
	cargo build --release
}

package() {
	install -Dm755 "${srcdir}/${_pkgname}/target/release/totalmapper" "${pkgdir}/usr/bin/totalmapper"
	install -Dm644 -t "${pkgdir}/usr/share/doc/${_pkgname}/" "${srcdir}/${_pkgname}/README.md"
}
