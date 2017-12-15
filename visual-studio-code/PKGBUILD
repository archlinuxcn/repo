# Maintainer: D. Can Celasun <can[at]dcc[dot]im>

pkgname=visual-studio-code
pkgver=1.19.0
pkgrel=1
pkgdesc="Visual Studio Code: Editor for building and debugging modern web and cloud applications (official binary version)"
arch=('x86_64' 'i686')
url="https://code.visualstudio.com/"
license=('custom: commercial')
provides=('vscode','visualstudiocode')
depends=(fontconfig libxtst gtk2 python cairo alsa-lib nss gcc-libs libnotify libxss gconf)
optdepends=('gvfs: Needed for move to trash functionality')
source_x86_64=(code_x64_${pkgver}.tar.gz::https://vscode-update.azurewebsites.net/${pkgver}/linux-x64/stable
               ${pkgname}.desktop
               )
source_i686=(code_ia32_${pkgver}.tar.gz::https://vscode-update.azurewebsites.net/${pkgver}/linux-ia32/stable
              ${pkgname}.desktop
              )
sha256sums_x86_64=('96a40ee148bc5d6bf3498b28067c2f8b32d8522538c0674abfa29984e94d3221'
                   'de88d95db3f55ce58ffd3c229cbde566099384d4f005cf887b00ccaeed605984')
sha256sums_i686=('a78bcae11d021054c1226b7859e139a9f38daceed7bc806de4f1aca16a6dd50c'
                 'de88d95db3f55ce58ffd3c229cbde566099384d4f005cf887b00ccaeed605984')
package() {
  _pkg=VSCode-linux-x64
  if [ "${CARCH}" = "i686" ]; then
    _pkg=VSCode-linux-ia32
  fi

  install -d "${pkgdir}/usr/share/licenses/${pkgname}"
  install -d "${pkgdir}/opt/${pkgname}"
  install -d "${pkgdir}/usr/bin"
  install -d "${pkgdir}/usr/share/applications"
  install -d "${pkgdir}/usr/share/icons" 

  install -m644 "${srcdir}/${_pkg}/resources/app/LICENSE.txt" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  install -m644 "${srcdir}/${_pkg}/resources/app/resources/linux/code.png" "${pkgdir}/usr/share/icons/${pkgname}.png"
  install -m644 "${srcdir}/${pkgname}.desktop" "${pkgdir}/usr/share/applications/${pkgname}.desktop"

  cp -r "${srcdir}/${_pkg}/"* "${pkgdir}/opt/${pkgname}" -R
  ln -s /opt/${pkgname}/bin/code "${pkgdir}"/usr/bin/code
}
