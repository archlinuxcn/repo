# Maintainer: Merrick Luo <merrick@luois.me>
pkgname=iease-music
pkgver=1.0.3
pkgrel=0
pkgdesc='Elegant neteaseMusic desktop app, Rock with NeteaseMusic.'
arch=('x86_64')
url='https://github.com/trazyn/ieaseMusic'
license=('MIT')
_rpmname="ieaseMusic-${pkgver}-linux-x86_64.rpm"
depends=('libxtst' 'gtk2' 'gconf' 'libxss' 'nss' 'python' 'alsa-lib' 'java-environment')
makedepends=()
options=()
source=("https://github.com/trazyn/ieaseMusic/releases/download/v${pkgver}/${_rpmname}")
sha1sums=('6dedb45af650e30f5d8af74aa20632eb4a059b7c')

package() {
	cp -r ${srcdir}/opt ${pkgdir}/
	cp -r ${srcdir}/usr ${pkgdir}/
	mkdir -p ${pkgdir}/usr/bin/
	ln -s /opt/ieaseMusic/iease-music ${pkgdir}/usr/bin/
}
