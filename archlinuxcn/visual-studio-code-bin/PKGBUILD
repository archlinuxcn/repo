# Maintainer: D. Can Celasun <can[at]dcc[dot]im>

pkgname=visual-studio-code-bin
_pkgname=visual-studio-code
pkgver=1.54.3
pkgrel=2
pkgdesc="Visual Studio Code (vscode): Editor for building and debugging modern web and cloud applications (official binary version)"
arch=('x86_64' 'i686' 'aarch64' 'armv7h')
url="https://code.visualstudio.com/"
license=('custom: commercial')
provides=('code')
conflicts=('code')
# lsof: need for terminal splitting, see https://github.com/Microsoft/vscode/issues/62991
depends=(libxkbfile gnupg gtk3 libsecret nss gcc-libs libnotify libxss glibc lsof)
optdepends=('glib2: Needed for move to trash functionality'
            'libdbusmenu-glib: Needed for KDE global menu')
source=(${_pkgname}.desktop ${_pkgname}-url-handler.desktop ${_pkgname}-workspace.xml)
source_x86_64=(code_x64_${pkgver}.tar.gz::https://update.code.visualstudio.com/${pkgver}/linux-x64/stable)
source_aarch64=(code_arm64_${pkgver}.tar.gz::https://update.code.visualstudio.com/${pkgver}/linux-arm64/stable)
source_armv7h=(code_armhf_${pkgver}.tar.gz::https://update.code.visualstudio.com/${pkgver}/linux-armhf/stable)

# i686 uses "latest" instead of a specific version as it's not always updated in a timely manner
source_i686=(code_ia32_${pkgver}.tar.gz::https://update.code.visualstudio.com/latest/linux-ia32/stable)
# This generates cleaner checksums
sha256sums=('fcb68f31ab791e0ae126c09e01f28fb428fbbbb7cc36c07dcd595d9562c22e96'
            'be3d123aacd575d8f836728266eb421ea70399d713d1fc30378dbc5602b519fb'
            '24ba09a6398c9781ed7cb6f1a9f6f38ec204899ba1f33db92638bf6d3cb0aed6')
sha256sums_x86_64=('7321623f71206f0b06e658ec19573a427949cd05ba409456e6c3c303d01aea3a')
sha256sums_i686=('64360439cc2fa596838062f7e6f9757b79d4b775a564f18bad6cbad154bf850c')
sha256sums_aarch64=('4ce8c38ba12678a8e0e9236976c73ccfb8dd00063f78e5198f1c56e52bc39913')
sha256sums_armv7h=('1be63412492cc086b59e9b5b06de3071bb7b1748879723ace43208f0494c6cc2')


package() {
  _pkg=VSCode-linux-x64
  if [ "${CARCH}" = "aarch64" ]; then
    _pkg=VSCode-linux-arm64
  fi
  if [ "${CARCH}" = "armv7h" ]; then
    _pkg=VSCode-linux-armhf
  fi
  if [ "${CARCH}" = "i686" ]; then
    _pkg=VSCode-linux-ia32
  fi

  install -d "${pkgdir}/usr/share/licenses/${_pkgname}"
  install -d "${pkgdir}/opt/${_pkgname}"
  install -d "${pkgdir}/usr/bin"
  install -d "${pkgdir}/usr/share/applications"
  install -d "${pkgdir}/usr/share/icons" 
  install -d "${pkgdir}/usr/share/mime/packages"

  install -m644 "${srcdir}/${_pkg}/resources/app/LICENSE.rtf" "${pkgdir}/usr/share/licenses/${_pkgname}/LICENSE.rtf"
  install -m644 "${srcdir}/${_pkg}/resources/app/resources/linux/code.png" "${pkgdir}/usr/share/icons/${_pkgname}.png"
  install -m644 "${srcdir}/${_pkgname}.desktop" "${pkgdir}/usr/share/applications/${_pkgname}.desktop"
  install -m644 "${srcdir}/${_pkgname}-url-handler.desktop" "${pkgdir}/usr/share/applications/${_pkgname}-url-handler.desktop"
  install -m644 "${srcdir}/${_pkgname}-workspace.xml" "${pkgdir}/usr/share/mime/packages/${pkgname}-workspace.xml"

  cp -r "${srcdir}/${_pkg}/"* "${pkgdir}/opt/${_pkgname}" -R
  ln -s /opt/${_pkgname}/bin/code "${pkgdir}"/usr/bin/code
}

post_install() {
  if hash update-mime-database 2>/dev/null; then
    update-mime-database /usr/share/mime
  fi
}
