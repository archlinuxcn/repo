# Maintainer: Metal A-wing <1 at 233 dot email>
# Contributor: Amr Hassan <amr.hassan@gmail.com>

pkgname=pyoxidizer
_name=PyOxidizer
pkgver=0.18.0
pkgrel=3
pkgdesc="A modern Python application packaging and distribution tool"
depends=('gcc-libs' 'openssl' 'zlib')
arch=('x86_64' 'i686' 'arm' 'armv6h' 'armv7h' 'aarch64')
url="https://github.com/indygreg/PyOxidizer"
license=('MIT')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/indygreg/${_name}/archive/pyoxidizer/${pkgver}.tar.gz")
sha512sums=('c863d2cd5e386176212c93a79b669e0ccd1a8ede53b121cc5947b122675cba925a8d3cd7ea92bec14a6401b97ae8ab063860c95fe1fecf36c059a5c61c831681')
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
