# Maintainer: Integral <integral@member.fsf.org>

pkgname=qefientrymanager
_srcname=QEFIEntryManager
pkgver=0.5.0
pkgrel=1
pkgdesc="A userspace cross-platform EFI boot entry management GUI App based on Qt"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/Inokinoki/${_srcname}"
license=('GPL-3.0-or-later')
depends=('qt6-base' 'efivar' 'hicolor-icon-theme' 'polkit')
makedepends=('git' 'cmake' 'qt6-declarative' 'qt6-tools' 'clang')
source=(
	"git+${url}.git#tag=v${pkgver}"
	"git+https://github.com/Inokinoki/qefivar.git"
)
sha256sums=('7b21744df9480c39a0418213fe14fe52694d919dae1f2cc46266891b53317e9c'
            'SKIP')

prepare() {
	cd "${_srcname}/"

	git submodule init
	git config submodule.qefivar.url "${srcdir}/qefivar/"
	git -c protocol.file.allow=always submodule update
}

build() {
	local cmake_options=(
		-B build
		-S "${_srcname}"
		-D CMAKE_BUILD_TYPE=None
		-D CMAKE_INSTALL_PREFIX=/usr
	)

	cmake "${cmake_options[@]}"
	cmake --build build
}

package() {
	DESTDIR="${pkgdir}" cmake --install build

	# Documentation
	install -Dm644 "${_srcname}/README.md" -t "${pkgdir}/usr/share/doc/${_pkgname}/"
}
