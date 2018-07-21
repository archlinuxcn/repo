# Maintainer: Vojtěch Aschenbrenner <v@asch.cz>

pkgname=eclipse-vrapper
pkgver=0.72.0
_pkgdir=0.72.0
_pkgdate=20170311
pkgrel=1
pkgdesc="Vim-like editing plugin for Eclipse"
arch=('any')
url="http://vrapper.sourceforge.net/home/"
license=('GPL3')
depends=('eclipse>=4.5')
source=(https://github.com/vrapper/vrapper/releases/download/${_pkgdir}/vrapper_${pkgver}_${_pkgdate}.zip)
sha256sums=('b907142f392d1f65a306e83a7b836c209a656ea421bec770221f685c17d1f0ad')


package() {
  local dest=${pkgdir}/usr/lib/eclipse/dropins/vrapper/eclipse
  install -d ${dest}
  cp -r ${srcdir}/{features,plugins,README.txt,LICENSE.txt,CHANGELOG.txt} ${dest}
}
