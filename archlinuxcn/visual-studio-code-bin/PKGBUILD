# Maintainer: D. Can Celasun <can[at]dcc[dot]im>

pkgname=visual-studio-code-bin
_pkgname=visual-studio-code
pkgver=1.37.1
pkgrel=2
pkgdesc="Visual Studio Code (vscode): Editor for building and debugging modern web and cloud applications (official binary version)"
arch=('x86_64')
url="https://code.visualstudio.com/"
license=('custom: commercial')
provides=('code')
conflicts=('code')
depends=(fontconfig libxtst gtk3 python cairo alsa-lib nss gcc-libs libnotify libxss 'glibc>=2.28-4' lsof)
optdepends=('glib2: Needed for move to trash functionality'
            'libdbusmenu-glib: Needed for KDE global menu')
source=(code_x64_${pkgver}.tar.gz::https://vscode-update.azurewebsites.net/${pkgver}/linux-x64/stable
               ${_pkgname}.desktop ${_pkgname}-url-handler.desktop
               code.png
               )
sha256sums=('1fed2fd28c517c07e28bdbd7b6851e26a115af81805661cec1b52fb0bb91e7da'
            '488592034dd5f979083bbd80788d33e253bb3ac3e52d50faee80e715a924a212'
            '727adaf263801462744c65bc0fad1b64ab31b3c96ed1a11e5b61bffbd5d71bc7'
            '7537330cec94b308feaa9bb66db45b5554b8379ec7dce83990521d2860bca4b2')
package() {
  _pkg=VSCode-linux-x64

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
  
  # XFCE bug workaround
  # see https://aur.archlinux.org/packages/visual-studio-code-bin/#comment-692211
  mkdir -p "${pkgdir}/usr/share/icons/hicolor/512x512/apps"
  install -m644 "${srcdir}/code.png" "${pkgdir}/usr/share/icons/hicolor/512x512/apps/visual-studio-code.png"
}
