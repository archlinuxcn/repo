# Maintainer: Vojtěch Aschenbrenner <v@asch.cz>

pkgname=eclipse-vrapper
pkgver=0.74.0
_pkgdir=0.74.0
_pkgdate=20181124
pkgrel=1
pkgdesc="Vim-like editing plugin for Eclipse"
arch=('any')
url="http://vrapper.sourceforge.net/home/"
license=('GPL3')
depends=('eclipse>=4.5')
source=(https://github.com/vrapper/vrapper/releases/download/${_pkgdir}/vrapper_${pkgver}_${_pkgdate}.zip)
md5sums=('c5f27a84cdeeac12c3ae6cac6ee1830d')


package() {
  local dest=${pkgdir}/usr/lib/eclipse/dropins/vrapper/eclipse
  install -d ${dest}
  cp -r ${srcdir}/{features,plugins,README.txt,LICENSE.txt,CHANGELOG.txt} ${dest}
}
