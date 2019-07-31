# Maintainer: edward-p <micro.fedora@gmail.com>
pkgname=deepin-wine32-tools
deepin_name=deepin-wine32-tools
pkgvers=2.18-18
pkgver=2.18_18
pkgrel=2
epoch=
pkgdesc="Deepin Wine Tools"
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
source=("https://mirrors.ustc.edu.cn/deepin/pool/non-free/d/deepin-wine/${deepin_name}_${pkgvers}_i386.deb")
noextract=("${deepin_name}_${pkgvers}_i386.deb")
md5sums=('352fedd4505c86fdc29b74e85fdc00dc')
validpgpkeys=()

prepare() {
	ar -x ${deepin_name}_${pkgvers}_i386.deb
	mkdir ${deepin_name}-${pkgvers}
	tar -xf data.tar.xz --directory="${deepin_name}-${pkgvers}"	
}

package() {
	cd "${deepin_name}-${pkgvers}"
	cp -r ./ ${pkgdir}/
}
