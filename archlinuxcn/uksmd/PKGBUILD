# Maintainer: Oleksandr Natalenko <oleksandr@natalenko.name>

pkgname=uksmd
pkgver=6.4.1
pkgrel=2
pkgdesc="Userspace KSM helper daemon"
url=https://codeberg.org/pf-kernel/uksmd
license=(GPL3)
arch=(x86_64)
depends=(systemd procps-ng libcap-ng)
optdepends=('uksmdstats: for parsing /sys KSM statistics')
makedepends=(meson)
source=(${url}/archive/v${pkgver}.tar.gz)
sha256sums=('a7ca393ada6c1c25a7af88129da84830124db7dd44c3911938dff310bcff4fb9')

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
