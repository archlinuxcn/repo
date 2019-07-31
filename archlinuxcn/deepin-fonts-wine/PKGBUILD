# Maintainer: wszqkzqk <wszqkzqk@gmail.com>
# Maintainer: skywol <skywol@qq.com>
pkgname=deepin-fonts-wine
pkgvers=2.18-18
pkgver=2.18_18
pkgrel=2
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
source=("https://mirrors.ustc.edu.cn/deepin/pool/non-free/d/deepin-wine/${pkgname}_${pkgvers}_all.deb")
noextract=("${pkgname}_${pkgvers}_all.deb")
md5sums=('6c79b2b28192a7968d0b529a21bef703')
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
