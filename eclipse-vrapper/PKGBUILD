# Maintainer: Vojtěch Aschenbrenner <v@asch.cz>

pkgname=eclipse-vrapper
pkgver=0.60.0
_pkgdir=0.60.0
_pkgdate=20151004
pkgrel=1
pkgdesc="Vim-like editing plugin for Eclipse"
arch=('any')
url="http://vrapper.sourceforge.net/home/"
license=('GPL3')
depends=('eclipse>=4.5')
source=(http://downloads.sourceforge.net/project/vrapper/vrapper/${_pkgdir}/vrapper_${pkgver}_${_pkgdate}.zip)
sha256sums=('77bd4225ab83861fec0a0c6cd06b4bf692c4add0ad06b137ca81ede1e43f0393')

package() {
  local dest=${pkgdir}/usr/lib/eclipse/dropins/vrapper/eclipse
  install -d ${dest}
  cp -r ${srcdir}/{features,plugins,README.txt,LICENSE.txt,CHANGELOG.txt} ${dest}
}
