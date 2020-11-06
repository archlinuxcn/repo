# Maintainer: wszqkzqk <wszqkzqk@gmail.com>
# Maintainer: Skywol <skywol@qq.com>
# Maintainer: luosoy <249799588@qq.com>

pkgname=deepin-wine-plugin
_pkgver=5.1.13-1
pkgver=5.1.13
pkgrel=1
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
source_i686=("https://cdn-package-store6.deepin.com/appstore/pool/appstore/d/deepin-wine-helper/${pkgname}_${_pkgver}_i386.deb")
source_x86_64=("https://cdn-package-store6.deepin.com/appstore/pool/appstore/d/deepin-wine-helper/${pkgname}_${_pkgver}_amd64.deb")
noextract=("${pkgname}_${_pkgver}_${_archext}.deb")
md5sums_i686=('49b4bd5eb50c547558ee66f58fd26c8c')
md5sums_x86_64=('18bce5ae4303e4f437f6da10ef908c22')
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