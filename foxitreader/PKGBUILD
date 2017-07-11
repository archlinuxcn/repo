# Maintainer: Muflone http://www.muflone.com/contacts/english/
# Contributor: Stephen Zhang <zsrkmyn at gmail dot com>
# Contributor: TDY <tdy@archlinux.info>

pkgname=foxitreader
pkgver=2.4.1.0609
_frrev_i686=r08f07f8
_frrev_x86_64=${_frrev_i686}
pkgrel=2
pkgdesc="A fast, secure and complete PDF viewer"
arch=('i686' 'x86_64')
url="https://www.foxitsoftware.com/products/pdf-reader/"
license=('custom:EULA')
makedepends=('qt-installer-framework' 'qt5-tools' 'p7zip')
depends=('libsecret' 'qt5-webkit')
source=("https://www.foxitsoftware.com/products/pdf-reader/eula.html"
        "${pkgname}.patch")
source_i686=("http://cdn09.foxitsoftware.com/pub/foxit/reader/desktop/linux/2.x/${pkgver%.*.*}/en_us/FoxitReader${pkgver}_Server_x86_enu_Setup.run.tar.gz"
             "${pkgname}-excluded_files-i686")
source_x86_64=("http://cdn09.foxitsoftware.com/pub/foxit/reader/desktop/linux/2.x/${pkgver%.*.*}/en_us/FoxitReader${pkgver}_Server_x64_enu_Setup.run.tar.gz"
               "${pkgname}-excluded_files-x86_64")
sha256sums=('c1485614de2b8087d14ab2d7b10e51faaaaf83a96f8bce6a0e1791effadf6079'
            'd85bfa4b293927975182aa6b1582ac064c5732711e5678d5f1ec35e65c78e6d1')
sha256sums_i686=('03dd1c4d248bd1782a9a9dd46836ffec9f38128b5f34ad3370a71d33fd87c9bc'
                 '63cc381589ac06d68b4464cfcc22f85b639957ed1e33320411e92a7582a787b4')
sha256sums_x86_64=('d8093dd3b3aeb4e788cbdff5f9d05d7557eb440810f6da6bdc4e23447d3a27ba'
                   'cc68c68441db44cceb5e9bcf9ab8e2851a209147e99b4e0a52133eda0e73a80c')

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

