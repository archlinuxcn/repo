# Maintainer: Victor Dmitriyev <mrvvitek@gmail.com>
# Contributor: Alucryd <alucryd at gmail dot com>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: Stefan Husmann <stefan-husmann at t-online dot de>

pkgname='jlatexmath'
pkgver='1.0.7'
pkgrel='1'
pkgdesc='Java API to display mathematical formulas written in LaTeX'
arch=('any')
url='https://github.com/opencollab/jlatexmath'
license=('custom:GPL2')
depends=('java-runtime')
# signing key isn't mentioned anywhere, although
source=(
"http://central.maven.org/maven2/org/scilab/forge/${pkgname}/${pkgver}/${pkgname}-${pkgver}.jar"{,.asc}
"${pkgname}-LICENSE::https://github.com/opencollab/jlatexmath/raw/${pkgver}/jlatexmath/LICENSE"
)
noextract=("${pkgname}-${pkgver}.jar")
# md5 and sha1 sums are in the maven repository
md5sums=('e4babd85c718a43b210808fd273de910'
         'SKIP'
         'SKIP')
sha1sums=('cf9786b1d813a64a4ad04befc0dae48b9cde8edb'
          'SKIP'
          'SKIP')
sha256sums=('6d04c3843fc98d2eea9ba4cff0be7b80540ca75c5a4e0b3463fd1219c48cc65d'
            'SKIP'
            '55a1524c2889cd2e2cdc9c345090973798782923e0dc022cb7e55e0dc2ba6e2a')
validpgpkeys=('531C276EDBD23014F325C4767BDB188864BB6E71') # David Moten

package() {
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}.jar" \
    "${pkgdir}/usr/share/java/${pkgname}/${pkgname}.jar"
  install -Dm644 "${srcdir}/${pkgname}-LICENSE" \
    "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
