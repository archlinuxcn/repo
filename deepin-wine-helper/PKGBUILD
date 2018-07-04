# Maintainer: Skywol <Skywol@qq.com>
# Maintainer: wszqkzqk <wszqkzqk@gmail.com>
pkgname=deepin-wine-helper
pkgver=1.1deepin12
pkgrel=1
epoch=
pkgdesc="Deepin Wine Helper"
arch=('i686' 'x86_64')
url="http://www.deepin.org"
license=('Proprietary')
groups=()
depends=('deepin-wine-plugin' 'deepin-wine-plugin-virtual')
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
source=("https://mirrors.ustc.edu.cn/deepin/pool/non-free/d/${pkgname}/${pkgname}_${pkgver}_i386.deb")
noextract=("${pkgname}_${pkgver}_i386.deb")
md5sums=('719d79d0f68f31a023e4110d85e6ef31')
validpgpkeys=()

prepare() {
	ar -x ${pkgname}_${pkgver}_i386.deb
	mkdir ${pkgname}-${pkgver}
	tar -xf data.tar.xz --directory="${pkgname}-${pkgver}"	
}

package() {
	cd "${pkgname}-${pkgver}"
	cp -r ./ ${pkgdir}/
}
