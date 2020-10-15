# Maintainer: D. Can Celasun <can[at]dcc[dot]im>

pkgname=visual-studio-code-bin
_pkgname=visual-studio-code
pkgver=1.50.1
pkgrel=1
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
source=(code_x64_${pkgver}.tar.gz::https://vscode-update.azurewebsites.net/${pkgver}/linux-x64/stable
               ${_pkgname}.desktop ${_pkgname}-url-handler.desktop)


source_x86_64=(code_x64_${pkgver}.tar.gz::https://vscode-update.azurewebsites.net/latest/linux-x64/stable
               ${_pkgname}.desktop ${_pkgname}-url-handler.desktop
               )
source_aarch64=(code_arm64_${pkgver}.tar.gz::https://vscode-update.azurewebsites.net/latest/linux-arm64/stable
               ${_pkgname}.desktop ${_pkgname}-url-handler.desktop
               )
source_armv7h=(code_armhf_${pkgver}.tar.gz::https://vscode-update.azurewebsites.net/latest/linux-armhf/stable
               ${_pkgname}.desktop ${_pkgname}-url-handler.desktop
               )
source_i686=(code_ia32_${pkgver}.tar.gz::https://vscode-update.azurewebsites.net/latest/linux-ia32/stable
              ${_pkgname}.desktop ${_pkgname}-url-handler.desktop
              )

sha256sums=('1d8449102bcb0e78f253bd508d880b179048ad2a9066e113fa23b3188821eb56'
            '0deefcb638e06c35a52e7e9fb8e19b2dc393f01e5c1c122d2938cddeb22cf8de'
            'be3d123aacd575d8f836728266eb421ea70399d713d1fc30378dbc5602b519fb')
sha256sums_x86_64=('1d8449102bcb0e78f253bd508d880b179048ad2a9066e113fa23b3188821eb56'
                   '0deefcb638e06c35a52e7e9fb8e19b2dc393f01e5c1c122d2938cddeb22cf8de'
                   'be3d123aacd575d8f836728266eb421ea70399d713d1fc30378dbc5602b519fb')
sha256sums_i686=('64360439cc2fa596838062f7e6f9757b79d4b775a564f18bad6cbad154bf850c'
                 '0deefcb638e06c35a52e7e9fb8e19b2dc393f01e5c1c122d2938cddeb22cf8de'
                 'be3d123aacd575d8f836728266eb421ea70399d713d1fc30378dbc5602b519fb')
sha256sums_aarch64=('410a76380cea071242f753d2d1d3fb5e85c9e9e54db6aa6388b21b8100e86ac8'
                    '0deefcb638e06c35a52e7e9fb8e19b2dc393f01e5c1c122d2938cddeb22cf8de'
                    'be3d123aacd575d8f836728266eb421ea70399d713d1fc30378dbc5602b519fb')
sha256sums_armv7h=('9a3ef47178090f5379203feb98ff05193228d7561d121b81d34b38c05c30de0c'
                   '0deefcb638e06c35a52e7e9fb8e19b2dc393f01e5c1c122d2938cddeb22cf8de'
                   'be3d123aacd575d8f836728266eb421ea70399d713d1fc30378dbc5602b519fb')


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

  install -m644 "${srcdir}/${_pkg}/resources/app/LICENSE.rtf" "${pkgdir}/usr/share/licenses/${_pkgname}/LICENSE.rtf"
  install -m644 "${srcdir}/${_pkg}/resources/app/resources/linux/code.png" "${pkgdir}/usr/share/icons/${_pkgname}.png"
  install -m644 "${srcdir}/${_pkgname}.desktop" "${pkgdir}/usr/share/applications/${_pkgname}.desktop"
  install -m644 "${srcdir}/${_pkgname}-url-handler.desktop" "${pkgdir}/usr/share/applications/${_pkgname}-url-handler.desktop"

  cp -r "${srcdir}/${_pkg}/"* "${pkgdir}/opt/${_pkgname}" -R
  ln -s /opt/${_pkgname}/bin/code "${pkgdir}"/usr/bin/code
}
