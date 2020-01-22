# Maintainer: Victor Dmitriyev <mrvvitek@gmail.com>
# Contributor: Alucryd <alucryd at gmail dot com>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: Stefan Husmann <stefan-husmann at t-online dot de>

pkgname='jlatexmath-fop'
pkgver='1.0.7'
pkgrel='1'
pkgdesc='JLaTeXMath FOP plugin'
arch=('any')
url='https://github.com/opencollab/jlatexmath'
license=('custom:GPL2')
depends=('java-runtime' 'jlatexmath')
# signing key isn't mentioned anywhere, it seems
# "http://central.maven.org/maven2/org/scilab/forge/jlatexmath-fop/${pkgver}/jlatexmath-fop-${pkgver}.jar.asc"
source=(
"https://repo1.maven.org/maven2/org/scilab/forge/${pkgname}/${pkgver}/${pkgname}-${pkgver}.jar"
"${pkgname}-LICENSE::https://github.com/opencollab/jlatexmath/raw/${pkgver}/jlatexmath-fop/LICENSE"
)
noextract=("${pkgname}-${pkgver}.jar")
# md5 and sha1 sums are in the maven repository
md5sums=('a20fd772af6e5fb39abb489b89f32190'
         'SKIP')
sha1sums=('19785e331bbf6da7340e6c0b9d66d74b745c6371'
          'SKIP')
sha256sums=('cd3302fd0d7f17d44b82555f87689846e0bb70814f0639aae3b976dfac145496'
            '19ef7e8f22cdcce860c966e4f57d751588105751bab288bd825b94a896b07916')


package() {
	install -Dm644 "${srcdir}/${pkgname}-${pkgver}.jar" \
    "${pkgdir}/usr/share/java/jlatexmath/${pkgname}.jar"
  install -Dm644 "${srcdir}/${pkgname}-LICENSE" \
    "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
