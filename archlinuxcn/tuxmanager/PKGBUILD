# Maintainer: George Hu <integral@archlinux.org>

pkgname=tuxmanager
_srcname=TuxManager
pkgver=1.0.6
pkgrel=1
pkgdesc="A Linux Task Manager alternative built with Qt6"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/benapetr/${_srcname}"
license=('GPL-3.0-or-later')
depends=('glibc' 'hicolor-icon-theme' 'libgcc' 'libstdc++' 'qt6-base')
makedepends=('qt6-tools')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('94a3815f9614469793660f83c974bd318dadb1174581fac3a1f7bbf535620f8b')

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
