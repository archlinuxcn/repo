# Maintainer: George Hu <integral@archlinux.org>

pkgname=tuxmanager
_srcname=TuxManager
pkgver=1.0.1
pkgrel=1
pkgdesc="A Linux Task Manager alternative built with Qt6"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/benapetr/${_srcname}"
license=('GPL-3.0-or-later')
depends=('glibc' 'hicolor-icon-theme' 'libgcc' 'libstdc++' 'qt6-base')
makedepends=('qt6-tools' 'imagemagick')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('9d5f20a7d1c5180a723054de66f903fe1c566e54e5040bfa90e09e121d87418d')

prepare() {
	sed -i 's/^Icon=.*/Icon=tux-manager/' "${_srcname}-${pkgver}/debian/tux-manager.desktop"
}

build() {
	cd "${_srcname}-${pkgver}/"
	qmake6 src/TuxManager.pro
	make
}

package() {
	cd "${_srcname}-${pkgver}/"
	install -Dm755 tux-manager -t "${pkgdir}/usr/bin/"
	install -Dm644 debian/tux-manager.desktop -t "${pkgdir}/usr/share/applications/"
	install -Dm644 <(magick src/linux_task_manager_256.ico -) "${pkgdir}/usr/share/icons/hicolor/256x256/apps/tux-manager.png"
}
