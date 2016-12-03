# Maintainer: Morten Linderud <morten@linderud.pw>
# Contributor: Andreas Krinke <andreas dot krinke at gmx dot de>
pkgname=gephi
pkgver=0.9.1
pkgrel=6
pkgdesc="An interactive graph visualization and exploration platform"
arch=('i686' 'x86_64')
url="http://gephi.org"
license=('CDDL' 'GPL3')
depends=('java-runtime' 'libxxf86vm' 'java-environment')
makedepends=()
options=(!strip)
source=("https://github.com/gephi/gephi/releases/download/v$pkgver/gephi-$pkgver-linux.tar.gz")
sha256sums=('f1d54157302df05a53b94e1518880c949c43ba4ab21e52d57f3edcbdaa06c7ee')

package() {
  cd "$srcdir/gephi-${pkgver}"
  install -d "${pkgdir}/usr/share/java/${pkgname}"
  cp -r * "${pkgdir}/usr/share/java/${pkgname}"
  install -d "${pkgdir}/usr/bin"
  ln -s "/usr/share/java/${pkgname}/bin/gephi" "${pkgdir}/usr/bin/gephi"

  find "${pkgdir}" -type f -iname \*.dll -delete
  find "${pkgdir}" -type f -iname \*.exe -delete
}
