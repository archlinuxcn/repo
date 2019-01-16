# Maintainer: Muflone http://www.muflone.com/contacts/english/
# Contributor: Stephen Zhang <zsrkmyn at gmail dot com>
# Contributor: TDY <tdy@archlinux.info>

pkgname=foxitreader
pkgver=2.4.4.0911
_foxitrevision=r057d814
pkgrel=1
pkgdesc="A fast, secure and complete PDF viewer"
arch=('x86_64')
url="https://www.foxitsoftware.com/products/pdf-reader/"
license=('custom:EULA')
depends=('libsecret' 'libxslt' 'libxcomposite' 'libgl' 'libxrender' 'gstreamer0.10-base'
         'libxi' 'libsm' 'fontconfig' 'dbus' 'openssl-1.0' 'desktop-file-utils')
makedepends=('p7zip' 'chrpath')
optdepends=('gtk2: use GTK+ dialogs under GTK+ based desktop environments')
source=("http://cdn09.foxitsoftware.com/pub/foxit/reader/desktop/linux/2.x/${pkgver%.*.*}/en_us/FoxitReader.enu.setup.${pkgver}.x64.run.tar.gz"
        "https://www.foxitsoftware.com/products/pdf-reader/eula.html"
        "${pkgname}.patch"
        "${pkgname}-excluded_files")
sha256sums=('6b579bd4ecdf86f7e70a009886c511da0b5085b831b0d6afc42442cabc249b90'
            '7814e03ea944f5ee5ff791e97c13446a5274989a1679758a92af0405d0fc7dce'
            'ee0f65819d00fea89f40112c769c704c7b663ff852e9d1d6e36d1b6d054d9c05'
            'e558529c6dbea047eee744b011ffcc214547c503896b14211ebf5f6309ef4e9f')

build() {
  local _file
  local _line
  local _position
  # Clean installer dir
  if [ -d "${pkgname}-installer" ]
  then
    rm -rf "${pkgname}-installer"
  fi
  mkdir "${pkgname}-installer"
  # Decompress .run installer
  _file="FoxitReader.enu.setup.${pkgver}(${_foxitrevision}).x64.run"
  LANG=C grep --only-matching --byte-offset --binary \
              --text $'7z\xBC\xAF\x27\x1C' "${_file}" | cut -f1 -d: | 
         while read _position
         do
           dd if="${_file}" \
              bs=1M iflag=skip_bytes status=none skip=${_position} \
              of="${pkgname}-installer/bin-${_position}.7z"
         done
  # Clean build dir
  if [ -d "${pkgname}-build" ]
  then
    rm -rf "${pkgname}-build"
  fi
  # Decompress 7z files (some files are damaged during the extraction)
  cd "${pkgname}-installer"
  install -m 755 -d "${srcdir}/${pkgname}-build"
  for _file in *.7z
  do
    7z -bd -bb0 -y x -o"${srcdir}/${pkgname}-build" ${_file} 1>/dev/null 2>&1 || true
  done
  # Apply final patches
  cd "${srcdir}/${pkgname}-build"
  patch -p1 --no-backup-if-mismatch -i "${srcdir}/${pkgname}.patch"
  # Remove insecure RPATH
  for _file in "lib/libFcitxQt5DBusAddons.so.1.0" \
               "lib/libQt5PrintSupport.so.5.3.2" \
               "platforminputcontexts/libfcitxplatforminputcontextplugin.so" \
               "printsupport/libcupsprintersupport.so"
  do
    echo "  -> Removing insecure RPATH from ${_file}"
    chrpath --delete "${_file}"
  done
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
    if [ "${_line::2}" = "# " ]
    then
      echo "  -> Removing excluded files from ${_line:2}..."
    elif [ -n "${_line}" -a "${_line::1}" != "#" ]
    then
      rm "${srcdir}/${pkgname}-build/${_line}"
    fi
  done < "${srcdir}/${pkgname}-excluded_files"
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

