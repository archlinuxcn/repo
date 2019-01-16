# Maintainer: Merrick Luo <merrick@luois.me>
pkgname=iease-music
pkgver=1.3.2
pkgrel=1
pkgdesc='Elegant neteaseMusic desktop app, Rock with NeteaseMusic.'
arch=('x86_64')
url='https://github.com/trazyn/ieaseMusic'
license=('MIT')
depends=('gconf' 'libnotify' 'nss' 'libxss' 'libappindicator-gtk3' 'libxtst')
#makedepends=('git' 'wget' 'rpmextract')
options=()
_rpmname="ieaseMusic-${pkgver}-linux-x86_64.rpm"
#source=("git://github.com/trazyn/ieaseMusic.git")
source=("https://github.com/trazyn/ieaseMusic/releases/download/v${pkgver}/${_rpmname}")
sha1sums=('562c3a3f5d7d531325c96c984844da97da939f7e')
install='iease-music.install'

#pkgver () {
#  cd "$srcdir"/ieaseMusic
#  git describe --tags `git rev-list --tags --max-count=1` | cut -c 2-
#}

package() {
#  cd ${srcdir}
#  _rpmname="ieaseMusic-${pkgver}-linux-x86_64.rpm"
#  wget "$url/releases/download/v${pkgver}/${_rpmname}"
#  rpmextract.sh ${_rpmname}
	cp -r ${srcdir}/opt ${pkgdir}/
	cp -r ${srcdir}/usr ${pkgdir}/
	mkdir -p ${pkgdir}/usr/bin/
	ln -s /opt/ieaseMusic/ieaseMusic ${pkgdir}/usr/bin/iease-music
}
