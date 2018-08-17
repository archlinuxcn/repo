# Maintainer: D. Can Celasun <can[at]dcc[dot]im>

pkgname=visual-studio-code-bin
_pkgname=visual-studio-code
pkgver=1.26.1
pkgrel=2
pkgdesc="Visual Studio Code: Editor for building and debugging modern web and cloud applications (official binary version)"
arch=('x86_64' 'i686')
url="https://code.visualstudio.com/"
license=('custom: commercial')
provides=('vscode' 'visualstudiocode' 'visual-studio-code')
replaces=('visual-studio-code')
conflicts=('visual-studio-code')
depends=(fontconfig libxtst gtk3 python cairo alsa-lib nss gcc-libs libnotify libxss gconf 'glibc>=2.28-4')
optdepends=('gvfs: Needed for move to trash functionality')
source_x86_64=(code_x64_${pkgver}.tar.gz::https://vscode-update.azurewebsites.net/${pkgver}/linux-x64/stable
               ${_pkgname}.desktop
               )
source_i686=(code_ia32_${pkgver}.tar.gz::https://vscode-update.azurewebsites.net/${pkgver}/linux-ia32/stable
              ${_pkgname}.desktop
              )
sha256sums_x86_64=('5ef2f82e1272b0008a446fc8f62f9693e2af7c83d5922883ecbfd8a9986fd40b'
                   '488592034dd5f979083bbd80788d33e253bb3ac3e52d50faee80e715a924a212')
sha256sums_i686=('16a9eb4582767c31ca92fce9d7ed97b960175d8a97db25fab3c8e56afec2f3bc'
                 '488592034dd5f979083bbd80788d33e253bb3ac3e52d50faee80e715a924a212')
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

  cp -r "${srcdir}/${_pkg}/"* "${pkgdir}/opt/${_pkgname}" -R
  ln -s /opt/${_pkgname}/bin/code "${pkgdir}"/usr/bin/code
}
