# Maintainer: wszqkzqk <wszqkzqk@gmail.com>
# Maintainer: Skywol <skywol@qq.com>
# Maintainer: luosoy <249799588@qq.com>

pkgname=deepin-wine-plugin-virtual
_pkgver=1.0deepin5
pkgver=1.0.5
pkgrel=1
epoch=
pkgdesc="Deepin Wine plugin virtual package"
arch=('i686' 'x86_64')
url="http://www.deepin.org"
license=('Proprietary')
groups=()
depends=('p7zip' 'python-dbus')
makedepends=('tar')
checkdepends=()
optdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=()
install=
changelog=
source=("https://community-packages.deepin.com/deepin/pool/non-free/d/${pkgname}/${pkgname}_${_pkgver}_all.deb")
noextract=("${pkgname}_${_pkgver}_all.deb")
md5sums=('eba265581c776930a955d0029b1c50c0')
validpgpkeys=()

prepare() {
	ar -x ${pkgname}_${_pkgver}_all.deb
	mkdir ${pkgname}-${pkgver}
	tar -xf data.tar.xz --directory="${pkgname}-${pkgver}"	
}

package() {
	cd "${pkgname}-${pkgver}"
	cp -r ./ ${pkgdir}/
}