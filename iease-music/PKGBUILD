# Maintainer: Merrick Luo <merrick@luois.me>
pkgname=iease-music
pkgver=1.1.2
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
sha1sums=('b80d9296e5f728be87aac5c66b08a8e92af44064')
install='iease-music.install'

package() {
	cp -r ${srcdir}/opt ${pkgdir}/
	cp -r ${srcdir}/usr ${pkgdir}/
	mkdir -p ${pkgdir}/usr/bin/
	ln -s /opt/ieaseMusic/iease-music ${pkgdir}/usr/bin/
}
