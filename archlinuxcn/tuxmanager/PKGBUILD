# Maintainer: George Hu <integral@archlinux.org>

pkgname=tuxmanager
_srcname=TuxManager
pkgver=1.0.0
pkgrel=1
pkgdesc="A Linux Task Manager alternative built with Qt6"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/benapetr/${_srcname}"
license=('GPL-3.0-or-later')
depends=('glibc' 'hicolor-icon-theme' 'libgcc' 'libstdc++' 'qt6-base')
makedepends=('qt6-tools' 'imagemagick')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('04da2393d8f0a5f3d94fab4e0e667a42773f1cf2900dbd7d4dfa1160fd2331c1')

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
