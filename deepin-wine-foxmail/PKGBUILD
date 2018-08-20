# Maintainer: Skywol <skywol@qq.com>
pkgname=deepin-wine-foxmail
_pkgname=deepin.com.foxmail
pkgver=7.2deepin3
pkgrel=1
epoch=
pkgdesc="Deepin Wine Foxmail 7.2."
arch=('i686' 'x86_64')
url="http://www.foxmail.com"
license=('Proprietary')
groups=()
depends=('deepin-wine')
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
source=("https://mirrors.ustc.edu.cn/deepin/pool/non-free/d/${_pkgname}/${_pkgname}_${pkgver}_i386.deb")
noextract=("${pkgname}_${pkgver}_i386.deb")
md5sums=('d339258b85a22bc36f59eaf85bb60d9a')
validpgpkeys=()

prepare() {
	ar -x ${_pkgname}_${pkgver}_i386.deb
	mkdir ${pkgname}-${pkgver}
	tar -xf data.tar.xz --directory="${pkgname}-${pkgver}"	
}

package() {
	cd "${pkgname}-${pkgver}"
	cp -r ./ ${pkgdir}/
}
