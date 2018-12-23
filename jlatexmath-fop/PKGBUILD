# Maintainer: Victor Dmitriyev <mrvvitek@gmail.com>
# Contributor: Alucryd <alucryd at gmail dot com>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: Stefan Husmann <stefan-husmann at t-online dot de>

pkgname='jlatexmath-fop'
pkgver='1.0.6'
pkgrel='1'
pkgdesc='JLaTeXMath FOP plugin'
arch=('any')
url='https://github.com/opencollab/jlatexmath'
license=('custom:GPL2')
depends=('java-runtime' 'jlatexmath')
# signing key isn't mentioned anywhere, it seems
# "http://central.maven.org/maven2/org/scilab/forge/jlatexmath-fop/${pkgver}/jlatexmath-fop-${pkgver}.jar.asc"
source=(
"http://central.maven.org/maven2/org/scilab/forge/${pkgname}/${pkgver}/${pkgname}-${pkgver}.jar"
"${pkgname}-LICENSE::https://github.com/opencollab/jlatexmath/raw/${pkgver}/jlatexmath-fop/LICENSE"
)
noextract=("${pkgname}-${pkgver}.jar")
# md5 and sha1 sums are in the maven repository
md5sums=('da4f8921338a724fe936d2168b59bd6c'
         'SKIP')
sha1sums=('80b68d66862a15978ef61220afec334e1176d5c6'
          'SKIP')
sha256sums=('a85bf2a8a37a00181b0079b2960379d19ad8c56c229a3d66bc61dd560487e69c'
            '19ef7e8f22cdcce860c966e4f57d751588105751bab288bd825b94a896b07916')


package() {
	install -Dm644 "${srcdir}/${pkgname}-${pkgver}.jar" \
    "${pkgdir}/usr/share/java/jlatexmath/${pkgname}.jar"
  install -Dm644 "${srcdir}/${pkgname}-LICENSE" \
    "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
