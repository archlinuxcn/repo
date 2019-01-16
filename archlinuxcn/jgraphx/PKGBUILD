# Maintainer: Victor Dmitriyev <mrvvitek@gmail.com>
# Contributor: Alucryd <alucryd at gmail dot com>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: Stefan Husmann <stefan-husmann at t-online dot de>

pkgname=jgraphx
pkgver=3.7.4
pkgrel=1
pkgdesc="Open source graph drawing component."
arch=('any')
url="https://github.com/jgraph/jgraphx"
license=('BSD')
depends=('java-runtime')
source=( "${pkgname}-v${pkgver}.tar.gz::https://github.com/jgraph/jgraphx/archive/v${pkgver}.tar.gz"
)
sha256sums=('e73f5ee1d8a380992206fa9fe19279c6ceff4c31172b188d268203888e65dfc3')

package() {
  cd "${srcdir}/jgraphx-${pkgver}"
	install -Dm644 "license.txt" \
    "${pkgdir}/usr/share/licenses/${pkgname}/license.txt"
	install -Dm644 "lib/jgraphx.jar" \
    "${pkgdir}/usr/share/java/${pkgname}/${pkgname}.jar"
}

# vim:set ts=2 sw=2 et:
