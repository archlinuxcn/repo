# Maintainer: Muflone http://www.muflone.com/contacts/english/
# Contributor: TDY <tdy@archlinux.info>

pkgname=foxitreader
epoch=1
pkgver=1.1.0.0225
_pkgver=1.10.0225
_pkgrev=205262
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
            'cd1c29f50086b9d754d925728207343f5a4d3d6bc13cef3679bb6e86244990a4')
sha256sums_i686=('16984a9b52537dcb57c2304441fca3a906a8bd7271f1f4919fcdc8a5dbdf9fc8')
sha256sums_x86_64=('2967571a4844ab834e03f9d63ee89c3df027ac16c8ae25e6f7affee70654c1cf')

build() {
  # Clean installer dir
  if [ -d "${pkgname}-installer" ]
  then
    rm -rf "${pkgname}-installer"
  fi
  # Decompress .run installer
  if [ "${CARCH}" = 'x86_64' ]
  then
    _file_run="FoxitReader.enu.setup.${pkgver}(r${_pkgrev}).x64.run"
  else
    _file_run="FoxitReader.enu.setup.${pkgver}(r${_pkgrev}).x86.run"
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
  # Apply final patches
  cd "${pkgdir}"
  patch -p1 -i "${srcdir}/${pkgname}.patch"
  # Remove useless files
  cd "${pkgdir}/usr/lib/${pkgname}"
  rm "lib/.directory" "Activation" "Activation.desktop" "Activation.sh" \
     "countinstalltion" "countinstalltion.sh" \
     "FoxitReader.sh" "installUpdate" "ldlibrarypath.sh" \
     "maintenancetool.sh" "Uninstall.desktop" \
     "Update.desktop" "updater" "updater.sh" \
     "manual/en_us/FoxitReader1.0_QuickGuide_Linux.pdf" \
     "manual/en_us/FoxitReader1.0_QuickGuide_OSX.pdf" \
     "manual/en_us/FoxitReader1.1_QuickGuide_OSX.pdf"
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
  ln -s "/usr/lib/${pkgname}/FoxitReader" "${pkgdir}/usr/bin/${pkgname}"
}

