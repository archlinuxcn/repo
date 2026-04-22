# Maintainer: George Hu <integral@archlinux.org>

pkgname=tuxmanager
_srcname=TuxManager
pkgver=1.0.5
pkgrel=1
pkgdesc="A Linux Task Manager alternative built with Qt6"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/benapetr/${_srcname}"
license=('GPL-3.0-or-later')
depends=('glibc' 'hicolor-icon-theme' 'libgcc' 'libstdc++' 'qt6-base')
makedepends=('qt6-tools')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('42400961b79b56fe8126177e799b9c1606045c975e5cdbab613ba005d1d3a3b5')

build() {
	cd "${_srcname}-${pkgver}/"
	qmake6 src/TuxManager.pro
	make
}

package() {
	cd "${_srcname}-${pkgver}/"
	install -Dm755 tux-manager -t "${pkgdir}/usr/bin/"
	install -Dm644 packaging/data/io.github.benapetr.TuxManager.desktop -t "${pkgdir}/usr/share/applications/"
	install -Dm644 src/tux_manager_icon.svg -t "${pkgdir}/usr/share/icons/hicolor/scalable/apps/"
}
