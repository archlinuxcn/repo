# Maintainer: wszqkzqk <wszqkzqk@gmail.com>
# Maintainer: Skywol <skywol@qq.com>

pkgname=deepin-wine
pkgvers=2.18-18
pkgver=2.18_18
pkgrel=2
epoch=
pkgdesc="Deepin Wine"
arch=('i686' 'x86_64')
url="http://www.deepin.org"
license=('Proprietary')
groups=()
depends=('deepin-wine32' 'deepin-wine32-preloader' 'deepin-wine32-tools'  'deepin-wine-binfmt' 'deepin-wine-helper' 'deepin-fonts-wine' 'deepin-libwine' 'deepin-wine-uninstaller' 'deepin-udis86' 'lib32-gettext' 'lib32-libxcursor' 'lib32-fontconfig'  'lib32-mesa' 'lib32-lcms2' 'lib32-libjpeg6' 'lib32-libpulse' 'lib32-alsa-plugins' 'lib32-libxml2' 'lib32-libxrandr'  'lib32-libxi'  'lib32-glu'  'lib32-libldap' 'p7zip')
makedepends=('tar')
checkdepends=()
optdepends=('lib32-freetype2-infinality-ultimate: for better font view')
provides=()
conflicts=()
replaces=()
backup=()
options=()
install=
changelog=
source=("https://mirrors.ustc.edu.cn/deepin/pool/non-free/d/${pkgname}/${pkgname}_${pkgvers}_all.deb")
noextract=("${pkgname}_${pkgvers}_all.deb")
md5sums=('765612a15ce251c7c293ce171a83f6b7')
validpgpkeys=()

prepare() {
	ar -x ${pkgname}_${pkgvers}_all.deb
	mkdir ${pkgname}-${pkgvers}
	tar -xf data.tar.xz --directory="${pkgname}-${pkgvers}"	
}

package() {
	cd "${pkgname}-${pkgvers}"
	cp ./lib ./usr/ -rf
	rm ./lib -rf
	cp -r ./ ${pkgdir}/
}
