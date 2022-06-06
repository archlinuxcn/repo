# Maintainer: Metal A-wing <1 at 233 dot email>
# Contributor: Amr Hassan <amr.hassan@gmail.com>

pkgname=pyoxidizer
_name=PyOxidizer
pkgver=0.22.0
pkgrel=1
pkgdesc="A modern Python application packaging and distribution tool"
depends=('gcc-libs' 'openssl' 'zlib')
arch=('x86_64' 'i686' 'arm' 'armv6h' 'armv7h' 'aarch64')
url="https://github.com/indygreg/PyOxidizer"
license=('MIT')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/indygreg/${_name}/archive/pyoxidizer/${pkgver}.tar.gz")
sha512sums=('f3c6a0cf658069b77bcc4ac914e8099ce63199daa723122189506d6cdd6f42bf0cd1a3cfd113eca9a0ae14d89de93a0e07d0d3f4cfadfe124c854af565f50a09')
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
