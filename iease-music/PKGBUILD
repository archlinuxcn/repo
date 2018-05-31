# Maintainer: Merrick Luo <merrick@luois.me>
pkgname=iease-music
pkgver=1.1.5
pkgrel=0
pkgdesc='Elegant neteaseMusic desktop app, Rock with NeteaseMusic.'
arch=('x86_64')
url='https://github.com/trazyn/ieaseMusic'
license=('MIT')
_rpmname="ieaseMusic-${pkgver}-linux-x86_64.rpm"
depends=()
makedepends=()
options=()
source=("https://github.com/trazyn/ieaseMusic/releases/download/v${pkgver}/${_rpmname}")
sha1sums=('cf6e6dc979a10a12dcc6bebe17a3e9b248b3d292')
install='iease-music.install'

package() {
	cp -r ${srcdir}/opt ${pkgdir}/
	cp -r ${srcdir}/usr ${pkgdir}/
	mkdir -p ${pkgdir}/usr/bin/
	ln -s /opt/ieaseMusic/iease-music ${pkgdir}/usr/bin/
}
