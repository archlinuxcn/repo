# Maintainer: wszqkzqk <wszqkzqk@gmail.com>
# Maintainer: Skywol <skywol@qq.com>
# Maintainer: luosoy <249799588@qq.com>

pkgname=deepin-wine-plugin
_pkgver=5.1.2-2+rebuild
pkgver=5.1.2
pkgrel=2
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
source_i686=("https://community-packages.deepin.com/deepin/pool/non-free/d/deepin-wine-helper/${pkgname}_${_pkgver}_i386.deb")
source_x86_64=("https://community-packages.deepin.com/deepin/pool/non-free/d/deepin-wine-helper/${pkgname}_${_pkgver}_amd64.deb")
noextract=("${pkgname}_${_pkgver}_${_archext}.deb")
md5sums_i686=('3de5d5c1ecec8f6431f56ee68426409d')
md5sums_x86_64=('48dedbc21ac74f5e6c689cc676b2784c')
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