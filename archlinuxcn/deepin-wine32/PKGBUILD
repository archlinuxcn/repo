# Maintainer: wszqkzqk <wszqkzqk@gmail.com>
# Maintainer: Skywol <skywol@qq.com>
pkgname=deepin-wine32
pkgvers=2.18-14~rc1
pkgver=2.18_14
pkgrel=1
epoch=
pkgdesc="Deepin Wine32"
arch=('i686' 'x86_64')
url="http://www.deepin.org"
license=('Proprietary')
groups=()
depends=('deepin-wine32-preloader')
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
source=("https://mirrors.ustc.edu.cn/deepin/pool/non-free/d/deepin-wine/${pkgname}_${pkgvers}_i386.deb")
noextract=("${pkgname}_${pkgvers}_i386.deb")
md5sums=('548ceec976bf32b271ed98f094652672')
validpgpkeys=()

prepare() {
	ar -x ${pkgname}_${pkgvers}_i386.deb
	mkdir ${pkgname}-${pkgvers}
	tar -xf data.tar.xz --directory="${pkgname}-${pkgvers}"	
}

package() {
	cd "${pkgname}-${pkgvers}"
	cp -r ./ ${pkgdir}/
}
