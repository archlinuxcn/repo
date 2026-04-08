# Maintainer: George Hu <integral@archlinux.org>

pkgname=tuxmanager
_srcname=TuxManager
pkgver=1.0.2
pkgrel=1
pkgdesc="A Linux Task Manager alternative built with Qt6"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/benapetr/${_srcname}"
license=('GPL-3.0-or-later')
depends=('glibc' 'hicolor-icon-theme' 'libgcc' 'libstdc++' 'qt6-base')
makedepends=('qt6-tools' 'imagemagick')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('8b2de657a867ff4f89b50cfa2b2e9361c77a10d43b704409d2a06cbc87c247a6')

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
