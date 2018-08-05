# Maintainer: Skywol <Skywol@qq.com>
pkgname=deepin-qq-eim
_pkgname=deepin.com.qq.b.eim
pkgver=1.90.2220deepin0
pkgrel=1
epoch=
pkgdesc="Deepin Wine QQEIM 1.90"
arch=('i686' 'x86_64')
url="http://b.qq.com/"
license=('Proprietary')
groups=()
depends=('deepin-wine')
makedepends=('tar')
checkdepends=()
optdepends=()
provides=()
conflicts=(deepin.com.qq.eim)
replaces=()
backup=()
options=()
install=
changelog=
source=("https://mirrors.ustc.edu.cn/deepin/pool/non-free/d/${_pkgname}/${_pkgname}_${pkgver}_i386.deb")
noextract=("${_pkgname}_${pkgver}_i386.deb")
md5sums=('c6e7c4990e25e6885cb55e3b19818d5c')
validpgpkeys=()

prepare() {
	ar -x ${_pkgname}_${pkgver}_i386.deb
	mkdir ${_pkgname}-${pkgver}
	tar -xf data.tar.xz --directory="${_pkgname}-${pkgver}"
}

package() {
	cd "${_pkgname}-${pkgver}"
	cp -r ./ ${pkgdir}/
}
