# Maintainer: Integral <integral@member.fsf.org>

pkgname=qefientrymanager
_srcname=QEFIEntryManager
pkgver=0.4.1
pkgrel=6
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
sha256sums=('c294231c0570c5a25d63ec140a472b8e1f070254fa143c7cc2af6968a4292d14'
            'SKIP')

prepare() {
	cd "${_srcname}/"

	git submodule init
	git config submodule.qefivar.url "${srcdir}/qefivar/"
	git -c protocol.file.allow=always submodule update

	mkdir -p build
}

build() {
	cd "${_srcname}/build/"
	cmake -DCMAKE_BUILD_TYPE=None -DCMAKE_INSTALL_PREFIX=/usr ..
	cmake --build .
}

package() {
	cd "${_srcname}/"
	DESTDIR="${pkgdir}" cmake --install build

	# Documentation
	install -Dm644 README.md -t "${pkgdir}/usr/share/doc/${_pkgname}/"
}
