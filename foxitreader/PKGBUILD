# Maintainer: Muflone http://www.muflone.com/contacts/english/
# Contributor: TDY <tdy@archlinux.info>

pkgname=foxitreader
epoch=1
pkgver=1.0.1.0925
_pkgver=1.01.0925
_pkgrev=189237
pkgrel=1
pkgdesc="A fast, secure and complete PDF viewer"
arch=('i686' 'x86_64')
url="http://www.foxitsoftware.com/Secure_PDF_Reader/"
license=('custom:EULA')
makedepends=('qt-installer-framework' 'qt5-tools' 'p7zip')
depends=('desktop-file-utils')
install="${pkgname}.install"
source=("https://www.foxitsoftware.com/products/pdf-reader/eula.html"
        "${pkgname}.patch")
source_i686=("http://cdn01.foxitsoftware.com/pub/foxit/reader/desktop/linux/1.x/${pkgver%.*.*}/en_us/FoxitReader${_pkgver}_Server_x86_enu_Setup.run.tar.gz")
source_x86_64=("http://cdn01.foxitsoftware.com/pub/foxit/reader/desktop/linux/1.x/${pkgver%.*.*}/en_us/FoxitReader${_pkgver}_Server_x64_enu_Setup.run.tar.gz")
sha256sums=('a5be3dc1cf27536de2c0fb5a0d640db349be32f48547b3cc56dcb5791fb278be'
            '95dfbe05398dffbbfd31302f15e1707545512a4abb4b78d0ce843e19759d8586')
sha256sums_i686=('a4821aee03c2fdac67fbbfef09eda8ab3deb21f97442048e3e11c035ad747ba2')
sha256sums_x86_64=('49684040892037154d9f53a611c72f9d0e3b9fe9a5b7a3e079063ca01903138f')

build() {
  # Clean installer dir
  if [ -d "${pkgname}-installer" ]
  then
    rm -rf "${pkgname}-installer"
  fi
  # Decompress .run installer
  if [ "${CARCH}" = 'x86_64' ]
  then
    _file_run="FoxitReader.enu.setup.x64.${pkgver}(r${_pkgrev}).run"
  else
    _file_run="FoxitReader.enu.setup.x86.${pkgver}(r${_pkgrev}).run"
  fi
  devtool --dump "${pkgname}-installer" "${_file_run}"
}

package() {
  cd "${pkgname}-installer/metadata/Install Foxit Reader"
  # Decompress files
  install -m 755 -d "${pkgdir}/usr/lib/${pkgname}"
  for file in *.7z
  do
    7z x -o"${pkgdir}/usr/lib/${pkgname}" ${file} > /dev/null
  done

  # Remove useless files
  cd "${pkgdir}/usr/lib/${pkgname}"
  rm "lib/.directory" "Activation.desktop" "Activation.sh" "installUpdate" \
     "maintenancetool.sh" "Uninstall.desktop" "Update.desktop" "updater" \
     "updater.sh" "manual/en_us/FoxitReader1.0_QuickGuide_OSX.pdf"
  # These files won't exist in every installer
  [ -e "Foxit Reader Startup.Log" ] && rm "Foxit Reader Startup.Log"
  # Install icon and desktop files
  install -m 755 -d "${pkgdir}/usr/share/pixmaps"
  install -m 644 "images/FoxitReader.png" \
    "${pkgdir}/usr/share/pixmaps/${pkgname}.png"
  install -m 755 -d "${pkgdir}/usr/share/applications"
  install -m 755 "FoxitReader.desktop" \
    "${pkgdir}/usr/share/applications/${pkgname}.desktop"
  # Install license file
  install -m 755 -d "${pkgdir}/usr/share/licenses/${pkgname}"
  install -m 644 -t "${pkgdir}/usr/share/licenses/${pkgname}" "${srcdir}/eula.html"
  # Install launcher script
  cd "${pkgdir}"
  install -m 755 -d "${pkgdir}/usr/bin"
  ln -s "/usr/lib/${pkgname}/FoxitReader.sh" "${pkgdir}/usr/bin/${pkgname}"
  # Apply final patches
  cd "${pkgdir}"
  patch -p2 -i "${srcdir}/${pkgname}.patch"
}

