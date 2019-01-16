# Maintainer: wszqkzqk <wszqkzqk@gmail.com>
# Maintainer: Skywol <skywol@qq.com>
pkgname=deepin-wine-plugin
_pkgver=1.0deepin2
pkgver=1.0.2
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
source_i686=("https://mirrors.ustc.edu.cn/deepin/pool/non-free/d/${pkgname}/${pkgname}_${_pkgver}_i386.deb")
source_x86_64=("https://mirrors.ustc.edu.cn/deepin/pool/non-free/d/${pkgname}/${pkgname}_${_pkgver}_amd64.deb")
noextract=("${pkgname}_${_pkgver}_${_archext}.deb")
md5sums_i686=('954c963c03c20e2729b8c4e73306bbae')
md5sums_x86_64=('47b248b17f0bad43aeab5464f646e0d4')
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
