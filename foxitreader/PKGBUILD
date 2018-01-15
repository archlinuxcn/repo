# Maintainer: Muflone http://www.muflone.com/contacts/english/
# Contributor: Stephen Zhang <zsrkmyn at gmail dot com>
# Contributor: TDY <tdy@archlinux.info>

pkgname=foxitreader
pkgver=2.4.1.0609
_foxitrevision=r08f07f8
pkgrel=6
pkgdesc="A fast, secure and complete PDF viewer"
arch=('x86_64')
url="https://www.foxitsoftware.com/products/pdf-reader/"
license=('custom:EULA')
depends=('libsecret' 'qt5-webkit')
source=("http://cdn09.foxitsoftware.com/pub/foxit/reader/desktop/linux/2.x/${pkgver%.*.*}/en_us/FoxitReader${pkgver}_Server_x64_enu_Setup.run.tar.gz"
        "https://www.foxitsoftware.com/products/pdf-reader/eula.html"
        "${pkgname}.patch"
        "${pkgname}-excluded_files-x86_64"
        "installer.qs")
sha256sums=('d8093dd3b3aeb4e788cbdff5f9d05d7557eb440810f6da6bdc4e23447d3a27ba'
            'c1485614de2b8087d14ab2d7b10e51faaaaf83a96f8bce6a0e1791effadf6079'
            'd85bfa4b293927975182aa6b1582ac064c5732711e5678d5f1ec35e65c78e6d1'
            'aac1c0aac453470bbfd1f65033a1fdaeb6eb660ba15e94cc10262c054bb9aa23'
            'afe2ca6ed0cec06256d329a1529e5d299eb289cb25132ef253d6d2e9b7489aa8')

prepare() {
  # Fix output path in the installer script
  sed "s#OUTPUT_DIRECTORY#${srcdir}/${pkgname}-installer#" "${srcdir}/installer.qs" > "${pkgname}.qs"
}

build() {
  local _line
  # Clean installer dir
  if [ -d "${pkgname}-installer" ]
  then
    rm -rf "${pkgname}-installer"
  fi
  # Decompress .run installer
  QT_QPA_PLATFORM=minimal "./FoxitReader.enu.setup.${pkgver}(${_foxitrevision}).x64.run" \
                          --script "${pkgname}.qs" "${srcdir}/${pkgname}-installer"
  # Fix desktop file path
  cd "${srcdir}/${pkgname}-installer"
  sed -i '/Exec=/d' FoxitReader.desktop
  # Apply final patches
  patch -p4 --no-backup-if-mismatch -i "${srcdir}/${pkgname}.patch"
  # Remove unneeded files
  rm "Activation" "Activation.desktop" "Activation.sh" \
     "countinstalltion" "countinstalltion.sh" \
     "installUpdate" \
     "maintenancetool" "maintenancetool.dat" "maintenancetool.ini" "maintenancetool.sh" \
     "Uninstall.desktop" \
     "Update.desktop" "updater" "updater.sh"
  find -type d -name ".svn" -exec rm -rf {} +
  find -type f -name ".directory" -exec rm -rf {} +
  find -type f -name "*~" -exec rm {} +
  # Remove excluded files
  while IFS='' read -r _line
  do
    if [ "${_line::2}" = "# " ]
    then
      echo "  -> Removing excluded files from ${_line:2}..."
    elif [ -n "${_line}" -a "${_line::1}" != "#" ]
    then
      rm "${srcdir}/${pkgname}-installer/${_line}"
    fi
  done < "${srcdir}/${pkgname}-excluded_files-$CARCH"
}

check() {
  # Check for unwanted libraries
  local _file
  local _unwanted=0
  cd "${srcdir}/${pkgname}-installer/lib"

  # Check if lib folders is not empty  
  if [ "$(ls -A .)" ]
  then
    ls -l
    # Check every library file
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
  fi
}

package() {
  install -m 755 -d "${pkgdir}/usr/lib/${pkgname}"
  cd "${srcdir}/${pkgname}-installer"
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

