# Maintainer: Muflone http://www.muflone.com/contacts/english/
# Contributor: Stephen Zhang <zsrkmyn at gmail dot com>
# Contributor: TDY <tdy@archlinux.info>

pkgname=foxitreader
pkgver=2.4.0.14978
_frrev_i686=r254978
_frrev_x86_64=${_frrev_i686}
pkgrel=1
pkgdesc="A fast, secure and complete PDF viewer"
arch=('i686' 'x86_64')
url="https://www.foxitsoftware.com/products/pdf-reader/"
license=('custom:EULA')
makedepends=('qt-installer-framework' 'qt5-tools' 'p7zip')
depends=('desktop-file-utils' 'qt5-declarative' 'libsecret')
source=("https://www.foxitsoftware.com/products/pdf-reader/eula.html"
        "${pkgname}.patch")
source_i686=("http://cdn09.foxitsoftware.com/pub/foxit/reader/desktop/linux/2.x/${pkgver%.*.*}/en_us/FoxitReader${pkgver}_Server_x86_enu_Setup.run.tar.gz")
source_x86_64=("http://cdn09.foxitsoftware.com/pub/foxit/reader/desktop/linux/2.x/${pkgver%.*.*}/en_us/FoxitReader${pkgver}_Server_x64_enu_Setup.run.tar.gz")
sha256sums=('738fc621a727e0429b9c50580b3c166776797f925f2819037d1414dad0b95f6a'
            'd85bfa4b293927975182aa6b1582ac064c5732711e5678d5f1ec35e65c78e6d1')
sha256sums_i686=('1804bfcd6b090bc416b815f9dc14488abca9f1cb3785406d250852a79c3972f4')
sha256sums_x86_64=('678a130e96a53f2b42d966b8e6c33c4563b0740db72d12876496b8657eb45fc4')

build() {
  # Clean installer dir
  if [ -d "${pkgname}-installer" ]
  then
    rm -rf "${pkgname}-installer"
  fi
  # Decompress .run installer
  if [ "${CARCH}" = 'x86_64' ]
  then
    _file_run="FoxitReader.enu.setup.${pkgver}(${_frrev_x86_64}).x64.run"
  else
    _file_run="FoxitReader.enu.setup.${pkgver}(${_frrev_i686}).x86.run"
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
  rm "Activation" "Activation.desktop" "Activation.sh" \
     "countinstalltion" "countinstalltion.sh" \
     "installUpdate" "ldlibrarypath.sh" \
     "maintenancetool.sh" "Uninstall.desktop" \
     "Update.desktop" "updater" "updater.sh"
  find -type d -name .svn -exec rm -rf {} +
  find -type f -name .directory -exec rm -rf {} +
  # Install icon and desktop files
  install -m 755 -d "${pkgdir}/usr/share/pixmaps"
  install -m 644 "images/FoxitReader.png" \
    "${pkgdir}/usr/share/pixmaps/${pkgname}.png"
  install -m 755 -d "${pkgdir}/usr/share/applications"
  install -m 755 "FoxitReader.desktop" \
    "${pkgdir}/usr/share/applications/${pkgname}.desktop"
  rm FoxitReader.desktop
  # Install license file
  install -m 755 -d "${pkgdir}/usr/share/licenses/${pkgname}"
  install -m 644 -t "${pkgdir}/usr/share/licenses/${pkgname}" "${srcdir}/eula.html"
  # Install launcher script
  cd "${pkgdir}"
  install -m 755 -d "${pkgdir}/usr/bin"
  ln -s "/usr/lib/${pkgname}/FoxitReader.sh" "${pkgdir}/usr/bin/${pkgname}"
}

