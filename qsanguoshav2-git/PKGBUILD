# Author: Moligaloo <Moligaloo@gmail.com>
# Maintainer: Iven Hsu <ivenvd@gmail.com>
# Contributor: Yangtse <yangtsesu@gmail.com>
# Contributor: Vehiclee <>
# Contributor: abf <zouxiaomingabf@gmail.com>

pkgname=qsanguoshav2-git
_gitname=QSanguosha-v2
pkgver=6017.bc669c2
pkgrel=3
pkgdesc="An open source online version of the famous board game Sanguosha"
arch=('i686' 'x86_64')
url="https://github.com/Mogara/QSanguosha-v2"
license=('GPL3')
depends=('qt5-quick1' 'phonon' 'plib' 'lua' 'fmodex')
makedepends=('git' 'swig')
conflicts=(qsanguosha)
provides=(qsanguosha)
source=('git://github.com/Mogara/QSanguosha-v2.git' 'qsanguosha' 'qsanguosha.desktop' 'sgs.png')
sha256sums=('SKIP'
            '37f60c732803dbb2ad156d3b301314b8238f7133cc944a842b1b31a5516eac90'
            '50897e23f6461b11b07968591b695009102a9052d6e3d9fc4a47b2258bf95f3e'
            '51f5b78572dce61831a47ab0ec8e0d0bb4fb87ae9f220c5fe5a00764118754c4')

pkgver() {
  cd $_gitname
  echo $(git rev-list --count master).$(git rev-parse --short master)
}

build() {
	cd ${srcdir}/${_gitname}
	qmake-qt5 .
	make
}

package() {
    cd ${srcdir}/${_gitname}
    mkdir -p ${pkgdir}/opt/qsanguosha
    cp -R {font,doc,audio,diy,etc,extension-doc,QSanguosha,qt_zh_CN.qm,image,lang,scenarios,lua,skins} ${pkgdir}/opt/qsanguosha/
    install -D -m755 ${srcdir}/qsanguosha "${pkgdir}/usr/bin/qsanguosha"
    install -D -m644 ${srcdir}/qsanguosha.desktop "${pkgdir}/usr/share/applications/qsanguosha.desktop"
    install -D -m644 ${srcdir}/sgs.png "${pkgdir}/usr/share/pixmaps/QSanguosha.png"
}

