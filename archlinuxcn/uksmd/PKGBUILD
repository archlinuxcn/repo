# Maintainer: Oleksandr Natalenko <oleksandr@natalenko.name>

pkgname=uksmd
pkgver=6.4
pkgrel=1
pkgdesc="Userspace KSM helper daemon"
url=https://codeberg.org/pf-kernel/uksmd
license=(GPL3)
arch=(x86_64)
depends=(systemd procps-ng libcap-ng)
makedepends=(meson)
source=(${url}/archive/v${pkgver}.tar.gz)
sha256sums=('12184d800df68d147186124f555a87f3ebfcf6de5aa9906e9e82bbd78c1c8129')

build() {
	cd ${pkgname}

	arch-meson . build

	meson compile -C build
}

package() {
	depends+=(UKSMD-BUILTIN)

	cd ${pkgname}

	meson install -C build --destdir "${pkgdir}"
}
