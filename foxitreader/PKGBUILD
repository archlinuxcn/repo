# Maintainer: Muflone http://www.muflone.com/contacts/english/
# Contributor: Stephen Zhang <zsrkmyn at gmail dot com>
# Contributor: TDY <tdy@archlinux.info>

pkgname=foxitreader
pkgver=2.4.0.14978
_frrev_i686=r254978
_frrev_x86_64=${_frrev_i686}
pkgrel=2
pkgdesc="A fast, secure and complete PDF viewer"
arch=('i686' 'x86_64')
url="https://www.foxitsoftware.com/products/pdf-reader/"
license=('custom:EULA')
makedepends=('qt-installer-framework' 'qt5-tools' 'p7zip')
depends=('libsecret' 'fcitx-qt5' 'qt5-webkit')
source=("https://www.foxitsoftware.com/products/pdf-reader/eula.html"
        "${pkgname}.patch")
source_i686=("http://cdn09.foxitsoftware.com/pub/foxit/reader/desktop/linux/2.x/${pkgver%.*.*}/en_us/FoxitReader${pkgver}_Server_x86_enu_Setup.run.tar.gz"
             "${pkgname}-excluded_files-i686")
source_x86_64=("http://cdn09.foxitsoftware.com/pub/foxit/reader/desktop/linux/2.x/${pkgver%.*.*}/en_us/FoxitReader${pkgver}_Server_x64_enu_Setup.run.tar.gz"
               "${pkgname}-excluded_files-x86_64")
sha256sums=('738fc621a727e0429b9c50580b3c166776797f925f2819037d1414dad0b95f6a'
            'd85bfa4b293927975182aa6b1582ac064c5732711e5678d5f1ec35e65c78e6d1')
sha256sums_i686=('1804bfcd6b090bc416b815f9dc14488abca9f1cb3785406d250852a79c3972f4'
                 'a3bc0169502fe781289af3ac9e15255e0a98b0d1fc68c93468c6e5e132ee50b2')
sha256sums_x86_64=('678a130e96a53f2b42d966b8e6c33c4563b0740db72d12876496b8657eb45fc4'
                   '578f1b93ae1eecb67d35f2f908abf0ca611656dbb8211a1be883a8ba01498dc1')

build() {
  local _file
  local _line
  # Clean installer dir
  if [ -d "${pkgname}-installer" ]
  then
    rm -rf "${pkgname}-installer"
  fi
  # Decompress .run installer
  if [ "${CARCH}" = 'x86_64' ]
  then
    _file="FoxitReader.enu.setup.${pkgver}(${_frrev_x86_64}).x64.run"
  else
    _file="FoxitReader.enu.setup.${pkgver}(${_frrev_i686}).x86.run"
  fi
  devtool --dump "${pkgname}-installer" "${_file}"
  # Clean build dir
  if [ -d "${pkgname}-build" ]
  then
    rm -rf "${pkgname}-build"
  fi
  # Decompress files
  cd "${pkgname}-installer/metadata/Install Foxit Reader"
  install -m 755 -d "${srcdir}/${pkgname}-build"
  for _file in *.7z
  do
    7z x -o"${srcdir}/${pkgname}-build" ${_file} > /dev/null
  done
  # Apply final patches
  cd "${srcdir}/${pkgname}-build"
  patch -p4 -i "${srcdir}/${pkgname}.patch"
  # Remove unneeded files
  rm "Activation" "Activation.desktop" "Activation.sh" \
     "countinstalltion" "countinstalltion.sh" \
     "installUpdate" "ldlibrarypath.sh" \
     "maintenancetool.sh" "Uninstall.desktop" \
     "Update.desktop" "updater" "updater.sh"
  find -type d -name ".svn" -exec rm -rf {} +
  find -type f -name ".directory" -exec rm -rf {} +
  find -type f -name "*~" -exec rm {} +
  # Remove excluded files
  while IFS='' read -r _line
  do
    if [ "${_line::1}" == '#' ]
    then
      echo "  -> Removing excluded files from ${_line:2}..."
    elif [ -n "${_line}" ]
    then
      rm "${srcdir}/${pkgname}-build/${_line}"
    fi
  done < "${srcdir}/${pkgname}-excluded_files-$CARCH"
}

check() {
  # Check for unwanted libraries
  local _file
  local _unwanted=0
  cd "${srcdir}/${pkgname}-build/lib"
  
  for _file in *
  do
    if [ "${_file}" != 'libQt5PrintSupport.so' -a \
         "${_file}" != 'libQt5PrintSupport.so.5' -a \
         "${_file}" != 'libQt5PrintSupport.so.5.3' -a \
         "${_file}" != 'libQt5PrintSupport.so.5.3.2' ]
    then
      echo "  -> Unwanted library ${_file}"
      _unwanted=1
    fi
  done
  if [ ${_unwanted} -ne 0 ]
  then
    echo "  -> At least an unwanted library exists in $PWD"
    exit 1
  fi
}

package() {
  install -m 755 -d "${pkgdir}/usr/lib/${pkgname}"
  cd "${srcdir}/${pkgname}-build"
  cp -r * "${pkgdir}/usr/lib/${pkgname}"
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

