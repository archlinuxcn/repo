# Maintainer: Vojtěch Aschenbrenner <v@asch.cz>

pkgname=eclipse-vrapper
pkgver=0.58.0
_pkgdir=0.58.0
_pkgdate=20150802
pkgrel=1
pkgdesc="Vim-like editing plugin for Eclipse"
arch=('any')
url="http://vrapper.sourceforge.net/home/"
license=('GPL3')
depends=('eclipse>=4.5')
source=(http://downloads.sourceforge.net/project/vrapper/vrapper/${_pkgdir}/vrapper_${pkgver}_${_pkgdate}.zip)
sha256sums=('a9b0c82da16453d1a55bf90d56b296ee749f51b40965d30b184f5e17829ed98e')

package() {
  local dest=${pkgdir}/usr/lib/eclipse/dropins/vrapper/eclipse
  install -d ${dest}
  cp -r ${srcdir}/{features,plugins,README.txt,LICENSE.txt,CHANGELOG.txt} ${dest}
}
