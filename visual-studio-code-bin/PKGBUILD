# Maintainer: D. Can Celasun <can[at]dcc[dot]im>

pkgname=visual-studio-code-bin
_pkgname=visual-studio-code
pkgver=1.30.1
pkgrel=1
pkgdesc="Visual Studio Code (vscode): Editor for building and debugging modern web and cloud applications (official binary version)"
arch=('x86_64' 'i686')
url="https://code.visualstudio.com/"
license=('custom: commercial')
provides=('code')
conflicts=('code')
depends=(fontconfig libxtst gtk3 python cairo alsa-lib nss gcc-libs libnotify libxss gconf 'glibc>=2.28-4' lsof)
optdepends=('gvfs: Needed for move to trash functionality'
            'libdbusmenu-glib: Needed for KDE global menu')
source_x86_64=(code_x64_${pkgver}.tar.gz::https://vscode-update.azurewebsites.net/${pkgver}/linux-x64/stable
               ${_pkgname}.desktop ${_pkgname}-url-handler.desktop
               )
source_i686=(code_ia32_${pkgver}.tar.gz::https://vscode-update.azurewebsites.net/${pkgver}/linux-ia32/stable
              ${_pkgname}.desktop ${_pkgname}-url-handler.desktop
              )
sha256sums_x86_64=('8ac8f4149c555def050bedcf32d0a260af6597925d6e8dd69cabb0f40d9be740'
                   '488592034dd5f979083bbd80788d33e253bb3ac3e52d50faee80e715a924a212'
                   '727adaf263801462744c65bc0fad1b64ab31b3c96ed1a11e5b61bffbd5d71bc7')
sha256sums_i686=('2b01605044ec3b7561505cb782ca214f55fed96e133851e91a856aeef09b4df5'
                 '488592034dd5f979083bbd80788d33e253bb3ac3e52d50faee80e715a924a212'
                 '727adaf263801462744c65bc0fad1b64ab31b3c96ed1a11e5b61bffbd5d71bc7')
package() {
  _pkg=VSCode-linux-x64
  if [ "${CARCH}" = "i686" ]; then
    _pkg=VSCode-linux-ia32
  fi

  install -d "${pkgdir}/usr/share/licenses/${_pkgname}"
  install -d "${pkgdir}/opt/${_pkgname}"
  install -d "${pkgdir}/usr/bin"
  install -d "${pkgdir}/usr/share/applications"
  install -d "${pkgdir}/usr/share/icons" 

  install -m644 "${srcdir}/${_pkg}/resources/app/LICENSE.txt" "${pkgdir}/usr/share/licenses/${_pkgname}/LICENSE"
  install -m644 "${srcdir}/${_pkg}/resources/app/resources/linux/code.png" "${pkgdir}/usr/share/icons/${_pkgname}.png"
  install -m644 "${srcdir}/${_pkgname}.desktop" "${pkgdir}/usr/share/applications/${_pkgname}.desktop"
  install -m644 "${srcdir}/${_pkgname}-url-handler.desktop" "${pkgdir}/usr/share/applications/${_pkgname}-url-handler.desktop"

  cp -r "${srcdir}/${_pkg}/"* "${pkgdir}/opt/${_pkgname}" -R
  ln -s /opt/${_pkgname}/bin/code "${pkgdir}"/usr/bin/code
}
