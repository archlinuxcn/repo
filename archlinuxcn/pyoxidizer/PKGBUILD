# Maintainer: Metal A-wing <1 at 233 dot email>
# Contributor: Amr Hassan <amr.hassan@gmail.com>

pkgname=pyoxidizer
_name=PyOxidizer
pkgver=0.20.0
pkgrel=1
pkgdesc="A modern Python application packaging and distribution tool"
depends=('gcc-libs' 'openssl' 'zlib')
arch=('x86_64' 'i686' 'arm' 'armv6h' 'armv7h' 'aarch64')
url="https://github.com/indygreg/PyOxidizer"
license=('MIT')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/indygreg/${_name}/archive/pyoxidizer/${pkgver}.tar.gz")
sha512sums=('54dd14fcdf0cf676185de9d567d55935c059df29e825eabea8ea105a17c9a79eaba9328f37e97691b9282abf18a2e943ecadb93d2b16be28311a5b74af58427b')
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
