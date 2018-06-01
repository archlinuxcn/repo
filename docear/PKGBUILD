# Maintainer: Roman Vasilev <2rvasilev@live.ru>
# Maintainer: Cloud Han <heliumhgy@gmail.com>

pkgname=docear
pkgver=1.2.0_stable
pkgrel=4
pkgdesc="Docear is an academic literature suite for searching, organizing and creating academic literature, built upon the mind mapping software Freeplane and the reference manager JabRef."
arch=('any')
url="http://www.docear.org/"
license=('GPL 2')
groups=()
depends=('jre8-openjdk-headless')
makedepends=()
optdepends=()
provides=('docear')
conflicts=()
replaces=()
backup=()
options=()
install=
changelog=
source=("${pkgname}_${pkgver}.tar.gz::http://docear.org/downloads/docear_linux.tar.gz"
        "https://www.dropbox.com/s/roqtejlo3b8gizg/docear-metadata-lib-0.0.1.jar?raw=1"
        "docear.desktop")
md5sums=('679747b7624e29efa0f82ca7fa96bc53'
         '0247fc67435670827a7ba0e86d409a4a'
         '6023a37923cd962f53db05ed5e2a6b21')
noextract=(docear-metadata-lib-0.0.1.jar?raw=1)

build() {
  # echo "Cleaning src directory..."
  # find "${srcdir}" -maxdepth 1 -mindepth 1 -type d  -exec rm -r {} \;
  # echo "Cleaned src directory"

  # bsdtar -xf "${pkgname}_${pkgver}.tar.gz"
  cd ${srcdir}
  rm `find . -name "docear-metadata-lib-0.0.1.jar"`
#  mv "docear-"* "docear"
#  cp -sr "docear-"* docear
}

package()
{

  install -dm 755 "${pkgdir}/usr/share/docear"
  cp -r "${srcdir}/docear-"*/* "${pkgdir}/usr/share/docear/"

  find "${pkgdir}/usr/share/docear" -type d -exec chmod 755 {} \;
  find "${pkgdir}/usr/share/docear" -type f -exec chmod 644 {} \;
  chmod 755 "${pkgdir}/usr/share/docear/docear.sh"
  
  sed -i -e 's/$(which java)/\/usr\/lib\/jvm\/java-8-openjdk\/jre\/bin\/java/g' "${pkgdir}/usr/share/docear/docear.sh"
  
  install -dm 755 "${pkgdir}/usr/bin"
  echo "#! /bin/sh" > "${pkgdir}/usr/bin/docear"
  echo "/usr/share/docear/docear.sh \$*" >> "${pkgdir}/usr/bin/docear"
  chmod 755 "${pkgdir}/usr/bin/docear"

  install -d "${pkgdir}/usr/share/applications"
  install -Dm 644 "$srcdir/docear.desktop" "${pkgdir}/usr/share/applications/docear.desktop"

  install -Dm 644 "$srcdir/docear-metadata-lib-0.0.1.jar?raw=1" "${pkgdir}/usr/share/docear/plugins/org.docear.plugin.bibtex/lib/docear-metadata-lib-0.0.1.jar"

  # enable antialiasing when start up docear
  echo "-Dawt.useSystemAAFontSettings=on" >> "${pkgdir}/usr/share/docear/init.xargs"
}
