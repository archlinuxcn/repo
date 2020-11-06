# Maintainer: wszqkzqk <wszqkzqk@gmail.com>
# Maintainer: Skywol <skywol@qq.com>
# Maintainer: luosoy <249799588@qq.com>

pkgname=deepin-wine-plugin-virtual
_pkgver=5.1.13-1
pkgver=5.1.13
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
source=("https://cdn-package-store6.deepin.com/appstore/pool/appstore/d/deepin-wine-helper/${pkgname}_${_pkgver}_all.deb")
noextract=("${pkgname}_${_pkgver}_all.deb")
md5sums=('b0b9c97c8f0f0c48b3e5eb11d3dba942')
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