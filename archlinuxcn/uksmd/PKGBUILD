# Maintainer: Oleksandr Natalenko <oleksandr@natalenko.name>

pkgname=uksmd
pkgver=6.5.1
pkgrel=1
pkgdesc="Userspace KSM helper daemon"
url=https://codeberg.org/pf-kernel/uksmd
license=(GPL3)
arch=(x86_64)
depends=(systemd procps-ng libcap-ng)
optdepends=('uksmdstats: for parsing /sys KSM statistics')
makedepends=(meson)
source=(${url}/archive/v${pkgver}.tar.gz)
sha256sums=('ca9dfc2ac7196b20571bba852ff7749592362d91f830b65a831ace18362f4ff1')

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
