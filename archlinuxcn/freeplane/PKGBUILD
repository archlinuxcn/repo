# Maintainer: Leonidas Spyropoulos (artafinde at gmail dot com)
# Contributor: scrawler@gmail.com

pkgname=freeplane
pkgver=1.8.11
pkgrel=1
pkgdesc="A Java mindmapping tool"
arch=('any')
url="http://freeplane.sourceforge.net"
license=('GPL')
makedepends=('unzip')
depends=('java-runtime>7' 'desktop-file-utils')
source=("https://downloads.sourceforge.net/sourceforge/${pkgname}/${pkgname}_bin-${pkgver}.zip"
        "freeplane.desktop" "freeplane.run")
b2sums=('9aa4faeeced23714cb0368e12ed7006a7d199494f9e9555666966dede64478814be608ef90ccc5ee398debb8d153166e33de2dd3bfd8d8408f5a83dc1e385b92'
        'f73371afd6fad2e105ecb7b3f802561b45ddb2e5401d82987876ee55bb9c15ed9995bfd013229de1cf731ec692bf52088a9a745c9e035d414e46c1868bdb2719'
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

  cd ${srcdir}/${pkgname}-${pkgver}
  # Copy plugins
  find plugins -type f | while read file ; do
    install -Dm644 "${file}" "${pkgdir}/usr/share/freeplane/${file}"
  done
  # Copy docs (excluding API JavaDocs)
  find doc -type f ! -path "*api*"| while read file; do
    install -Dm644 "${file}" "${pkgdir}/usr/share/freeplane/${file}"
  done
  # Copy various
  install -Dm644 ${srcdir}/${pkgname}-${pkgver}/framework.jar ${pkgdir}/usr/share/freeplane/framework.jar
  install -Dm644 ${srcdir}/${pkgname}-${pkgver}/freeplane.l4j.ini ${pkgdir}/usr/share/freeplane/freeplane.l4j.ini
  install -Dm755 ${srcdir}/${pkgname}-${pkgver}/freeplane.policy ${pkgdir}/usr/share/freeplane/freeplane.policy
  install -Dm755 ${srcdir}/${pkgname}-${pkgver}/freeplane.sh ${pkgdir}/usr/share/freeplane/freeplane.sh
  install -Dm644 ${srcdir}/${pkgname}-${pkgver}/freeplaneConsole.l4j.ini ${pkgdir}/usr/share/freeplane/freeplaneConsole.l4j.ini
  install -Dm644 ${srcdir}/${pkgname}-${pkgver}/freeplaneIcons.dll ${pkgdir}/usr/share/freeplane/freeplaneIcons.dll
  install -Dm644 ${srcdir}/${pkgname}-${pkgver}/freeplanelauncher.jar ${pkgdir}/usr/share/freeplane/freeplanelauncher.jar
  install -Dm644 ${srcdir}/${pkgname}-${pkgver}/gitinfo.txt ${pkgdir}/usr/share/freeplane/gitinfo.txt
  install -Dm644 ${srcdir}/${pkgname}-${pkgver}/init.xargs ${pkgdir}/usr/share/freeplane/init.xargs
  install -Dm644 ${srcdir}/${pkgname}-${pkgver}/license.txt ${pkgdir}/usr/share/freeplane/licence.txt
  install -Dm644 ${srcdir}/${pkgname}-${pkgver}/props.xargs ${pkgdir}/usr/share/freeplane/props.xargs
  # Copy core
  install -Dm644 ${srcdir}/${pkgname}-${pkgver}/core/org.freeplane.core/META-INF/* ${pkgdir}/usr/share/freeplane/core/org.freeplane.core/META-INF/
  install -Dm644 ${srcdir}/${pkgname}-${pkgver}/core/org.freeplane.core/lib/* ${pkgdir}/usr/share/freeplane/core/org.freeplane.core/lib
  # Copy resources
  install -Dm644 ${srcdir}/${pkgname}-${pkgver}/resources/ortho/* ${pkgdir}/usr/share/freeplane/resources/ortho/
  install -Dm644 ${srcdir}/${pkgname}-${pkgver}/resources/templates/* ${pkgdir}/usr/share/freeplane/resources/templates/
  install -Dm644 ${srcdir}/${pkgname}-${pkgver}/resources/xslt/* ${pkgdir}/usr/share/freeplane/resources/xslt/
  install -Dm644 ${srcdir}/${pkgname}-${pkgver}/resources/xml/* ${pkgdir}/usr/share/freeplane/resources/xml/
  install -Dm644 ${srcdir}/${pkgname}-${pkgver}/resources/gitinfo.properties ${pkgdir}/usr/share/freeplane/resources/gitinfo.properties
  # Copy scripts
  install -Dm644 ${srcdir}/${pkgname}-${pkgver}/scripts/* ${pkgdir}/usr/share/freeplane/scripts/
  
  # Install the desktop entry
  install -Dm644 ${srcdir}/freeplane.desktop ${pkgdir}/usr/share/applications/freeplane.desktop
  # Install icons
  install -Dm644 ${srcdir}/${pkgname}-${pkgver}/freeplane.svg ${pkgdir}/usr/share/pixmaps/freeplane.svg
  # Install the executable script
  install -Dm755 ${srcdir}/freeplane.run ${pkgdir}/usr/bin/freeplane
}
