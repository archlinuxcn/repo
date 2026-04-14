# Maintainer: George Hu <integral@archlinux.org>

pkgname=tuxmanager
_srcname=TuxManager
pkgver=1.0.4
pkgrel=2
pkgdesc="A Linux Task Manager alternative built with Qt6"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/benapetr/${_srcname}"
license=('GPL-3.0-or-later')
depends=('glibc' 'hicolor-icon-theme' 'libgcc' 'libstdc++' 'qt6-base')
makedepends=('qt6-tools')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('634d721139c9042549cd8d41b01feb595c88e81029437cda780faea4a3201b08')

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
	install -Dm644 src/tux_manager_icon.svg "${pkgdir}/usr/share/icons/hicolor/scalable/apps/tux-manager.svg"
}
