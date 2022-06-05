# Maintainer: Metal A-wing <1 at 233 dot email>
# Contributor: Amr Hassan <amr.hassan@gmail.com>

pkgname=pyoxidizer
_name=PyOxidizer
pkgver=0.21.0
pkgrel=1
pkgdesc="A modern Python application packaging and distribution tool"
depends=('gcc-libs' 'openssl' 'zlib')
arch=('x86_64' 'i686' 'arm' 'armv6h' 'armv7h' 'aarch64')
url="https://github.com/indygreg/PyOxidizer"
license=('MIT')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/indygreg/${_name}/archive/pyoxidizer/${pkgver}.tar.gz")
sha512sums=('6f4115f900c18182fa40eba63c7813aeca8b96b8a7e99c679d0da3a33c6cf705f5538547b85095ec64dc6756ac531dcf6afffab9757e3d83d1a85960dd4024cc')
makedepends=('cargo' 'python3')

build() {
   cd "${_name}-${pkgname}-${pkgver}"
   cargo build --bin pyoxidizer --release --locked
}

check() {
   cd "${_name}-${pkgname}-${pkgver}"

	 # For `extra-x86_64-build`
	 # This test used stdout extra-x86_64-build is failure

	 # For `makepkg`
	 # Can be used, no problem
	 # cargo test --bin pyoxidizer --release --locked
}

package() {
   cd "${_name}-${pkgname}-${pkgver}"
   install -Dm 755 target/release/${pkgname} -t "${pkgdir}/usr/bin"
}
