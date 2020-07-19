# Maintainer: wszqkzqk <wszqkzqk@gmail.com>
# Maintainer: Skywol <skywol@qq.com>
# Maintainer: luosoy <249799588@qq.com>

pkgname=deepin-wine-plugin
_pkgver=1.0deepin4
pkgver=1.0.4
pkgrel=4
epoch=
pkgdesc="Deepin Wine plugin"
arch=('i686' 'x86_64')
url="http://www.deepin.org"
license=('Proprietary')
groups=()
depends=('gtk2')
makedepends=('tar')
checkdepends=()
optdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=('!emptydirs')
install=
changelog=
[[ "$CARCH" = "i686" ]] && _archext=i386 || _archext=amd64
source_i686=("https://community-packages.deepin.com/deepin/pool/non-free/d/${pkgname}/${pkgname}_${_pkgver}_i386.deb")
source_x86_64=("https://community-packages.deepin.com/deepin/pool/non-free/d/${pkgname}/${pkgname}_${_pkgver}_amd64.deb")
noextract=("${pkgname}_${_pkgver}_${_archext}.deb")
md5sums_i686=('89066af2323d471bd03512c28708dc8b')
md5sums_x86_64=('8f18569625c93790b9d1b46b9e03afcd')
validpgpkeys=()

prepare() {
	ar -x ${pkgname}_${_pkgver}_${_archext}.deb
	mkdir ${pkgname}-${pkgver}
	tar -xf data.tar.xz --directory="${pkgname}-${pkgver}"	
}

package() {
	cd "${pkgname}-${pkgver}"
	cp -r ./ ${pkgdir}/
}