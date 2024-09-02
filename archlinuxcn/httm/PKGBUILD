# Maintainer: xgjmibzr <xgjmibzr@gmail.com>

pkgname=httm
pkgver=0.42.3
pkgrel=1
pkgdesc="Prints the size, date and locations of available unique versions (deduplicated by modify time and size) of files residing on ZFS or BTRFS snapshots."
arch=('x86_64')
url="https://github.com/kimono-koans/httm"
license=('MPL-2.0')
conflicts=('httm-bin' 'httm-git')
options=('!strip' '!emptydirs')
#install='httm.install'
depends=('gcc-libs')
optdepends=('btrfs-progs: BTRFS support'
            'zfs-utils: ZFS support'
            'nilfs-utils: NILFS2 support')
makedepends=('cargo')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/${pkgver}.tar.gz")
sha512sums=('2f5da3ec56084a38b3644881687f7e12568a17fa4aa1adbe451f9ba7249c4ac59b33cda9438ca5208bb1f13eaf57e164e3c7de590b7ba0e79438f6832730cf17')

prepare() {
	cd "${srcdir}/${pkgname}-${pkgver}"
	cargo fetch --target "$CARCH-unknown-linux-gnu"
}

build(){
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	# use cargo to build from a tagged release
	cd "${srcdir}/${pkgname}-${pkgver}"
	cargo build --frozen --release --all-features
}

package(){
	# install executable
	install -Dm755 "${srcdir}/${pkgname}-${pkgver}/target/release/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"

	# install man page
	install -Dm644 "${srcdir}/${pkgname}-${pkgver}/${pkgname}.1" "${pkgdir}/usr/share/man/man1/${pkgname}.1"

	# install README.md
	install -Dm644 "${srcdir}/${pkgname}-${pkgver}/README.md" "${pkgdir}/usr/share/doc/${pkgname}/README.md"

	# install LICENSE
	install -Dm644 "${srcdir}/${pkgname}-$pkgver/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
