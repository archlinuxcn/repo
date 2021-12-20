# Maintainer: Leonidas Spyropoulos (artafinde at gmail dot com)
# Contributor: scrawler@gmail.com

pkgname=freeplane
pkgver=1.9.12
pkgrel=1
pkgdesc="A Java mindmapping tool"
arch=('any')
url="http://freeplane.sourceforge.net"
license=('GPL2')
makedepends=('gradle' 'jdk11-openjdk' 'gnu-free-fonts' 'fontconfig')
depends=('java-runtime>7' 'desktop-file-utils')
source=("https://downloads.sourceforge.net/sourceforge/${pkgname}/${pkgname}_src-${pkgver}.tar.gz"
        "freeplane.desktop" "freeplane.run")
b2sums=('f04980e46ffd1641b26f1269a0b020b11776142f9d14bfe619fa420dd94ab32d5efa54872d678776b60ab77257798423c72a810eef0d3403101310e40bfcea96'
        '87c25331e01823e38668e4b394a51a279c05b24b088f4ffc1482d3783e24018da8f9e51b3ad1a62c5a863f85a6ccb30bbe8999cb861dc1b93d5483019644cfa5'
        '24ca56b7c7894b9bb38600b4d37973769243e1bdb221f33125b60bf4f878a3b630775710fab9dee97fa45a69319455037e294860ba7fbd608529982c6b0b1538')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  export JAVA_HOME=/usr/lib/jvm/java-11-openjdk
  export PATH="${JAVA_HOME}/bin:${PATH}"
  gradle -Dorg.gradle.daemon=false build
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}/BIN"
  # Copy plugins
  find plugins -type f | while read file ; do
    install -Dm644 "${file}" "${pkgdir}/usr/share/freeplane/${file}"
  done
  # Copy docs (excluding API JavaDocs)
  find doc -type f ! -path "*api*"| while read file; do
    install -Dm644 "${file}" "${pkgdir}/usr/share/freeplane/${file}"
  done
  # Copy various
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}/BIN"/framework.jar "${pkgdir}"/usr/share/freeplane/framework.jar
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}/BIN"/freeplane.l4j.ini "${pkgdir}"/usr/share/freeplane/freeplane.l4j.ini
  install -Dm755 "${srcdir}/${pkgname}-${pkgver}/BIN"/freeplane.policy "${pkgdir}"/usr/share/freeplane/freeplane.policy
  install -Dm755 "${srcdir}/${pkgname}-${pkgver}/BIN"/freeplane.sh "${pkgdir}"/usr/share/freeplane/freeplane.sh
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}/BIN"/freeplaneConsole.l4j.ini "${pkgdir}"/usr/share/freeplane/freeplaneConsole.l4j.ini
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}/BIN"/freeplaneIcons.dll "${pkgdir}"/usr/share/freeplane/freeplaneIcons.dll
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}/BIN"/freeplanelauncher.jar "${pkgdir}"/usr/share/freeplane/freeplanelauncher.jar
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}/BIN"/gitinfo.txt "${pkgdir}"/usr/share/freeplane/gitinfo.txt
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}/BIN"/init.xargs "${pkgdir}"/usr/share/freeplane/init.xargs
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}/BIN"/props.xargs "${pkgdir}"/usr/share/freeplane/props.xargs
  # Copy core
  install -dm755 "${pkgdir}"/usr/share/freeplane/core/org.freeplane.core/META-INF/
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}/BIN"/core/org.freeplane.core/META-INF/* "${pkgdir}"/usr/share/freeplane/core/org.freeplane.core/META-INF/
  install -dm755 "${pkgdir}"/usr/share/freeplane/core/org.freeplane.core/lib
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}/BIN"/core/org.freeplane.core/lib/* "${pkgdir}"/usr/share/freeplane/core/org.freeplane.core/lib
  # Copy resources
  install -dm755 "${pkgdir}"/usr/share/freeplane/resources/ortho/
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}/BIN"/resources/ortho/* "${pkgdir}"/usr/share/freeplane/resources/ortho/
  install -dm755 "${pkgdir}"/usr/share/freeplane/resources/templates/
  install -dm755 "${pkgdir}"/usr/share/freeplane/resources/templates/
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}/BIN"/resources/templates/* "${pkgdir}"/usr/share/freeplane/resources/templates/
  install -dm755 "${pkgdir}"/usr/share/freeplane/resources/xslt/
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}/BIN"/resources/xslt/* "${pkgdir}"/usr/share/freeplane/resources/xslt/
  install -dm755 "${pkgdir}"/usr/share/freeplane/resources/xml/
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}/BIN"/resources/xml/* "${pkgdir}"/usr/share/freeplane/resources/xml/
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}/BIN"/resources/gitinfo.properties "${pkgdir}"/usr/share/freeplane/resources/gitinfo.properties
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}/BIN"/resources/linkDecoration.ini "${pkgdir}"/usr/share/freeplane/resources/linkDecoration.ini
  # Copy scripts
  install -dm755 "${pkgdir}"/usr/share/freeplane/scripts/
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}/BIN"/scripts/* "${pkgdir}"/usr/share/freeplane/scripts/
  
  # Install the desktop entry
  install -Dm644 "${srcdir}"/freeplane.desktop "${pkgdir}"/usr/share/applications/freeplane.desktop
  # Install icons
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}/BIN"/freeplane.svg "${pkgdir}"/usr/share/pixmaps/freeplane.svg
  # Install the executable script
  install -Dm755 "${srcdir}"/freeplane.run "${pkgdir}"/usr/bin/freeplane
}
