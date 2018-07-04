# Maintainer: wszqkzqk <wszqkzqk@gmail.com>
# Maintainer: Skywol <skywol@qq.com>
pkgname=deepin-wine
deepin_name=deepin-wine
pkgvers=2.18-12
pkgver=2.18_12
pkgrel=1
epoch=
pkgdesc="Deepin Wine"
arch=('i686' 'x86_64')
url="http://www.deepin.org"
license=('Proprietary')
groups=()
depends=('deepin-wine32' 'deepin-wine32-preloader' 'deepin-wine32-tools'  'deepin-wine-binfmt' 'deepin-wine-helper' 'deepin-fonts-wine' 'deepin-libwine' 'deepin-wine-uninstaller' 'deepin-udis86' 'lib32-gettext' 'lib32-libxcursor' 'lib32-fontconfig' 'lib32-alsa-lib' 'lib32-mesa' 'lib32-lcms2' 'lib32-libjpeg6' 'lib32-libxml2' 'lib32-libxrandr' 'lib32-libxdamage' 'lib32-libxi' 'lib32-gettext' 'lib32-glu' 'lib32-libsm' 'lib32-libpcap' 'lib32-libldap' 'p7zip')
makedepends=('tar')
checkdepends=()
optdepends=('lib32-freetype2-infinality-ultimate: for better font view')
provides=()
conflicts=('deepin-wine')
replaces=()
backup=()
options=()
install=
changelog=
source=("https://mirrors.ustc.edu.cn/deepin/pool/non-free/d/${deepin_name}/${deepin_name}_${pkgvers}_all.deb")
noextract=("${deepin_name}_${pkgvers}_all.deb")
md5sums=('4c72927cc348b94e7fdcba9b23a59b9e')
validpgpkeys=()

prepare() {
	ar -x ${deepin_name}_${pkgvers}_all.deb
	mkdir ${deepin_name}-${pkgvers}
	tar -xf data.tar.xz --directory="${deepin_name}-${pkgvers}"	
}

package() {
	cd "${deepin_name}-${pkgvers}"
	cp ./lib ./usr/ -rf
	rm ./lib -rf
	cp -r ./ ${pkgdir}/
}
