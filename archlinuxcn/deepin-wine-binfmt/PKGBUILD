# Maintainer: Skywol <skywol@qq.com>
# Maintainer: wszqkzqk <wszqkzqk@gmail.com>
pkgname=deepin-wine-binfmt
deepin_name=deepin-wine-binfmt
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
source=("https://mirrors.ustc.edu.cn/deepin/pool/non-free/d/deepin-wine/${deepin_name}_${pkgvers}_all.deb")
noextract=("${deepin_name}_${pkgvers}_all.deb")
md5sums=('2d4eae0d2c99526c0aaef3c63cad0237')
validpgpkeys=()

prepare() {
	ar -x ${deepin_name}_${pkgvers}_all.deb
	mkdir ${deepin_name}-${pkgvers}
	tar -xf data.tar.xz --directory="${deepin_name}-${pkgvers}"	
}

package() {
	cd "${deepin_name}-${pkgvers}"
	cp -r ./ ${pkgdir}/
}
