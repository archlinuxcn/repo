# Maintainer: Vojtěch Aschenbrenner <v@asch.cz>

pkgname=eclipse-vrapper
pkgver=0.68.0
_pkgdir=0.68.0
_pkgdate=20160604
pkgrel=1
pkgdesc="Vim-like editing plugin for Eclipse"
arch=('any')
url="http://vrapper.sourceforge.net/home/"
license=('GPL3')
depends=('eclipse>=4.5')
source=(http://downloads.sourceforge.net/project/vrapper/vrapper/${_pkgdir}/vrapper_${pkgver}_${_pkgdate}.zip)
md5sums=('e268c7aaec5934e8b5c70ec7b14ab8db')

package() {
  local dest=${pkgdir}/usr/lib/eclipse/dropins/vrapper/eclipse
  install -d ${dest}
  cp -r ${srcdir}/{features,plugins,README.txt,LICENSE.txt,CHANGELOG.txt} ${dest}
}
