# Maintainer: Alexander 'z33ky' Hirsch <1zeeky@gmail.com>

pkgname=racerd-git
pkgver=99.0e18f33
pkgrel=1
pkgdesc='JSON/HTTP Server based on racer for adding Rust support to editors and IDEs'
arch=(i686 x86_64)
url='https://jwilm.github.io/racerd/libracerd/'
license=('Apache')
depends=('rust-racer')
makedepends=('git' 'rust' 'cargo')
source=('git+git://github.com/jwilm/racerd')
sha256sums=('SKIP')

pkgver() {
	cd "${srcdir}/racerd"
	printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
	cd "${srcdir}/racerd"
	cargo build --release
}

package() {
	cd "${srcdir}/racerd"
	cargo install --root "${pkgdir}/usr"
}
