# Maintainer:  Devin Cofer <ranguvar[at]ranguvar[dot]io>
# Contributor: DriverX
# Contributor: Nicolas Quiénot <niQo @ aur>
# Contributor: Martin Schrodt <martin@schrodt.org>
pkgname=nvme-cli
pkgver=1.7
pkgrel=1
pkgdesc="NVM-Express user space tooling for Linux"
arch=('i686' 'x86_64')
url="https://github.com/linux-nvme/nvme-cli"
license=('GPL')
depends=('systemd')
makedepends=('git')
conflicts=('nvme-cli-git')
source=("https://github.com/linux-nvme/${pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('3a139d40ffff48d2f0b06339fd3be3ed219241ce6838f0ea173d7459c9984ea2')

build() {
	cd "${srcdir}/${pkgname}-${pkgver}"
	CFLAGS="${CFLAGS} -I." make PREFIX=/usr
}

package() {
	cd "${srcdir}/${pkgname}-${pkgver}"
	make DESTDIR="${pkgdir}" PREFIX=/usr SBINDIR=/usr/bin install
}
