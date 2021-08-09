# Maintainer: Metal A-wing <1 at 233 dot email>
# Contributor: Amr Hassan <amr.hassan@gmail.com>

pkgname=pyoxidizer
_name=PyOxidizer
pkgver=0.17
pkgrel=1
pkgdesc="A modern Python application packaging and distribution tool"
depends=('gcc-libs' 'openssl' 'zlib')
arch=('x86_64' 'i686' 'arm' 'armv6h' 'armv7h' 'aarch64')
url="https://github.com/indygreg/PyOxidizer"
license=('MIT')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/indygreg/${_name}/archive/pyoxidizer/${pkgver}.tar.gz")
sha512sums=('d68ddbfc8ae3cb1da23a922a4621e7877e0b1af711413efc21e2a2fd8d7f76bf5b7b1cf92be5a2db4e8e8be850eda59b584d24705d8c99d5425a60bba0ec893a')
makedepends=(cargo)

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
