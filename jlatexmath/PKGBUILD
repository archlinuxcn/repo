# Maintainer: Victor Dmitriyev <mrvvitek@gmail.com>
# Contributor: Alucryd <alucryd at gmail dot com>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: Stefan Husmann <stefan-husmann at t-online dot de>

pkgname='jlatexmath'
pkgver='1.0.6'
pkgrel='1'
pkgdesc='Java API to display mathematical formulas written in LaTeX'
arch=('any')
url='https://github.com/opencollab/jlatexmath'
license=('custom:GPL2')
depends=('java-runtime')
# signing key isn't mentioned anywhere, it seems
# "http://central.maven.org/maven2/org/scilab/forge/${pkgname}/${pkgver}/${pkgname}-${pkgver}.jar.asc"
source=(
"http://central.maven.org/maven2/org/scilab/forge/${pkgname}/${pkgver}/${pkgname}-${pkgver}.jar"
"${pkgname}-LICENSE::https://github.com/opencollab/jlatexmath/raw/${pkgver}/jlatexmath/LICENSE"
)
noextract=("${pkgname}-${pkgver}.jar")
# md5 and sha1 sums are in the maven repository
md5sums=('60134d8ff0e88da339f7af13db551089'
         'SKIP')
sha1sums=('91eb47098174a4645f48abafac2e227bdf8fd605'
          'SKIP')
sha256sums=('f6367b5c99311cd38819a183d4eeae9df036ebf4ee6cc0eea5363cd2d31a5c20'
            '55a1524c2889cd2e2cdc9c345090973798782923e0dc022cb7e55e0dc2ba6e2a')


package() {
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}.jar" \
    "${pkgdir}/usr/share/java/${pkgname}/${pkgname}.jar"
  install -Dm644 "${srcdir}/${pkgname}-LICENSE" \
    "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
