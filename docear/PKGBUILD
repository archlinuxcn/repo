# Maintainer: Cloud Han <heliumhgy@gmail.com>

pkgname=docear
pkgver=1.1.0_stable
pkgrel=1
pkgdesc="Docear is an academic literature suite for searching, organizing and creating academic literature, built upon the mind mapping software Freeplane and the reference manager JabRef."
arch=('any')
url="http://www.docear.org/"
license=('GPL 2')
groups=()
depends=('java-runtime')
makedepends=()
optdepends=()
provides=('docear')
conflicts=()
replaces=()
backup=()
options=()
install=
changelog=
source=("${pkgname}_${pkgver}.tar.gz::http://sourceforge.net/projects/docear/files/1.x/${pkgver}/${pkgname}_linux.tar.gz/download"
        "docear.desktop")
md5sums=('d2429a48c4df9fbbfc5dfac6e10983eb'
         '6023a37923cd962f53db05ed5e2a6b21')
noextract=()

build() {
  # echo "Cleaning src directory..."
  # find "${srcdir}" -maxdepth 1 -mindepth 1 -type d  -exec rm -r {} \;
  # echo "Cleaned src directory"

  # bsdtar -xf "${pkgname}_${pkgver}.tar.gz"
  mv "docear-"* "docear-${pkgver}"
} 

package() {
  install -dm 755 "${pkgdir}/usr/share/docear"
  cp -r "${srcdir}/docear-${pkgver}"/* "${pkgdir}/usr/share/docear"
  find "${pkgdir}/usr/share/docear" -type d -exec chmod 755 {} \;
  find "${pkgdir}/usr/share/docear" -type f -exec chmod 644 {} \;
  chmod 755 "${pkgdir}/usr/share/docear/docear.sh"
  
  install -dm 755 "${pkgdir}/usr/bin"
  echo "#! /bin/sh" > "${pkgdir}/usr/bin/docear"
  echo "/usr/share/docear/docear.sh \$*" >> "${pkgdir}/usr/bin/docear"
  chmod 755 "${pkgdir}/usr/bin/docear"
  
  install -d "${pkgdir}/usr/share/applications"
  install -Dm 644 "$startdir/docear.desktop" "${pkgdir}/usr/share/applications/docear.desktop"
  
  # enable antialiasing when start up docear
  echo "-Dawt.useSystemAAFontSettings=on" >> "${pkgdir}/usr/share/docear/init.xargs"
}
