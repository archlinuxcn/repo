# Maintainer: wszqkzqk <wszqkzqk@gmail.com>
# Maintainer: skywol <skywol@qq.com>
# Maintainer: luosoy <249799588@qq.com>

pkgname=deepin-fonts-wine
pkgvers=2.18-24~rc3
pkgver=2.18_24
pkgrel=3
epoch=
pkgdesc="Deepin Wine Fonts"
arch=('i686' 'x86_64')
url="http://www.deepin.org"
license=('Proprietary')
groups=()
depends=()
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
source=("https://community-packages.deepin.com/deepin/pool/main/d/deepin-wine/${pkgname}_${pkgvers}_all.deb")
noextract=("${pkgname}_${pkgvers}_all.deb")
md5sums=('f4c46c61f844a58913f78c2a268141da')
validpgpkeys=()

prepare() {
	ar -x ${pkgname}_${pkgvers}_all.deb
	mkdir ${pkgname}-${pkgvers}
	tar -xf data.tar.xz --directory="${pkgname}-${pkgvers}"	
}

package() {
	cd "${pkgname}-${pkgvers}"
	cp -r ./ ${pkgdir}/
}