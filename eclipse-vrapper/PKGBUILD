# Maintainer: Vojtěch Aschenbrenner <v@asch.cz>

pkgname=eclipse-vrapper
pkgver=0.66.0
_pkgdir=0.66.0
_pkgdate=20160403
pkgrel=1
pkgdesc="Vim-like editing plugin for Eclipse"
arch=('any')
url="http://vrapper.sourceforge.net/home/"
license=('GPL3')
depends=('eclipse>=4.5')
source=(http://downloads.sourceforge.net/project/vrapper/vrapper/${_pkgdir}/vrapper_${pkgver}_${_pkgdate}.zip)
md5sums=('894dc1705bc72eada154819111fff593')

package() {
  local dest=${pkgdir}/usr/lib/eclipse/dropins/vrapper/eclipse
  install -d ${dest}
  cp -r ${srcdir}/{features,plugins,README.txt,LICENSE.txt,CHANGELOG.txt} ${dest}
}
