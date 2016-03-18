# Maintainer: Vojtěch Aschenbrenner <v@asch.cz>

pkgname=eclipse-vrapper
pkgver=0.64.0
_pkgdir=0.64.0
_pkgdate=20160201
pkgrel=1
pkgdesc="Vim-like editing plugin for Eclipse"
arch=('any')
url="http://vrapper.sourceforge.net/home/"
license=('GPL3')
depends=('eclipse>=4.5')
source=(http://downloads.sourceforge.net/project/vrapper/vrapper/${_pkgdir}/vrapper_${pkgver}_${_pkgdate}.zip)
md5sums=('994ab4c53d5e0099aec19ba7165a5605')

package() {
  local dest=${pkgdir}/usr/lib/eclipse/dropins/vrapper/eclipse
  install -d ${dest}
  cp -r ${srcdir}/{features,plugins,README.txt,LICENSE.txt,CHANGELOG.txt} ${dest}
}
