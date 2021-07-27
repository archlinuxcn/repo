# Maintainer: Leonidas Spyropoulos (artafinde at gmail dot com)
# Contributor: scrawler@gmail.com

pkgname=freeplane
pkgver=1.9.6
pkgrel=1
pkgdesc="A Java mindmapping tool"
arch=('any')
url="http://freeplane.sourceforge.net"
license=('GPL')
makedepends=('unzip')
depends=('java-runtime>7' 'desktop-file-utils')
source=("https://downloads.sourceforge.net/sourceforge/${pkgname}/${pkgname}_bin-${pkgver}.zip"
        "freeplane.desktop" "freeplane.run")
b2sums=('e9a4ac86060188663c44cb3c1ec2ab4ece91748de55a78363106e4763172010c4b03ca2cc57e20cac508b79dd5f92b1ce97ecd5ef795a0dd500f0a7a36b52825'
        '87c25331e01823e38668e4b394a51a279c05b24b088f4ffc1482d3783e24018da8f9e51b3ad1a62c5a863f85a6ccb30bbe8999cb861dc1b93d5483019644cfa5'
        '24ca56b7c7894b9bb38600b4d37973769243e1bdb221f33125b60bf4f878a3b630775710fab9dee97fa45a69319455037e294860ba7fbd608529982c6b0b1538')
package() {
  # Create required directories
  mkdir -p "${pkgdir}/usr/share/freeplane/core/org.freeplane.core/META-INF"
  mkdir -p "${pkgdir}/usr/share/freeplane/core/org.freeplane.core/lib"
  mkdir -p "${pkgdir}/usr/share/freeplane/resources/ortho"
  mkdir -p "${pkgdir}/usr/share/freeplane/resources/templates"
  mkdir -p "${pkgdir}/usr/share/freeplane/resources/xslt"
  mkdir -p "${pkgdir}/usr/share/freeplane/resources/xml"
  mkdir -p "${pkgdir}/usr/share/freeplane/scripts"
  mkdir -p "${pkgdir}/usr/share/freeplane/doc/Images/doc"
  mkdir -p "${pkgdir}/usr/share/freeplane/doc/Images/mouse"
  mkdir -p "${pkgdir}/usr/share/freeplane/doc/Images/other/workspace/output"

  cd "${srcdir}/${pkgname}-${pkgver}"
  # Copy plugins
  find plugins -type f | while read file ; do
    install -Dm644 "${file}" "${pkgdir}/usr/share/freeplane/${file}"
  done
  # Copy docs (excluding API JavaDocs)
  find doc -type f ! -path "*api*"| while read file; do
    install -Dm644 "${file}" "${pkgdir}/usr/share/freeplane/${file}"
  done
  # Copy various
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}"/framework.jar "${pkgdir}"/usr/share/freeplane/framework.jar
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}"/freeplane.l4j.ini "${pkgdir}"/usr/share/freeplane/freeplane.l4j.ini
  install -Dm755 "${srcdir}/${pkgname}-${pkgver}"/freeplane.policy "${pkgdir}"/usr/share/freeplane/freeplane.policy
  install -Dm755 "${srcdir}/${pkgname}-${pkgver}"/freeplane.sh "${pkgdir}"/usr/share/freeplane/freeplane.sh
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}"/freeplaneConsole.l4j.ini "${pkgdir}"/usr/share/freeplane/freeplaneConsole.l4j.ini
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}"/freeplaneIcons.dll "${pkgdir}"/usr/share/freeplane/freeplaneIcons.dll
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}"/freeplanelauncher.jar "${pkgdir}"/usr/share/freeplane/freeplanelauncher.jar
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}"/gitinfo.txt "${pkgdir}"/usr/share/freeplane/gitinfo.txt
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}"/init.xargs "${pkgdir}"/usr/share/freeplane/init.xargs
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}"/license.txt "${pkgdir}"/usr/share/freeplane/licence.txt
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}"/props.xargs "${pkgdir}"/usr/share/freeplane/props.xargs
  # Copy core
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}"/core/org.freeplane.core/META-INF/* "${pkgdir}"/usr/share/freeplane/core/org.freeplane.core/META-INF/
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}"/core/org.freeplane.core/lib/* "${pkgdir}"/usr/share/freeplane/core/org.freeplane.core/lib
  # Copy resources
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}"/resources/ortho/* "${pkgdir}"/usr/share/freeplane/resources/ortho/
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}"/resources/templates/* "${pkgdir}"/usr/share/freeplane/resources/templates/
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}"/resources/xslt/* "${pkgdir}"/usr/share/freeplane/resources/xslt/
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}"/resources/xml/* "${pkgdir}"/usr/share/freeplane/resources/xml/
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}"/resources/gitinfo.properties "${pkgdir}"/usr/share/freeplane/resources/gitinfo.properties
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}"/resources/linkDecoration.ini "${pkgdir}"/usr/share/freeplane/resources/linkDecoration.ini
  # Copy scripts
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}"/scripts/* "${pkgdir}"/usr/share/freeplane/scripts/
  
  # Install the desktop entry
  install -Dm644 "${srcdir}"/freeplane.desktop "${pkgdir}"/usr/share/applications/freeplane.desktop
  # Install icons
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}"/freeplane.svg "${pkgdir}"/usr/share/pixmaps/freeplane.svg
  # Install the executable script
  install -Dm755 "${srcdir}"/freeplane.run "${pkgdir}"/usr/bin/freeplane
}
