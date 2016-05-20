# Maintainer: D. Can Celasun <dcelasun[at]gmail[dot]com>

pkgname=visual-studio-code
pkgver=1.1.1
pkgrel=2
pkgdesc="Editor for building and debugging modern web and cloud applications"
arch=('x86_64' 'i686')
url="https://code.visualstudio.com/"
license=('custom: commercial')
provides=('vscode','visualstudiocode')
depends=(fontconfig libxtst gtk2 python cairo alsa-lib gconf nss gcc-libs libnotify)
_release=def9e32467ad6e4f48787d38caf190acbfee5880
source_x86_64=(VSCode-linux64_${pkgver}.zip::https://az764295.vo.msecnd.net/stable/$_release/VSCode-linux-x64-stable.zip
               ${pkgname}.desktop
               )
source_i686=(VSCode-linux32_${pkgver}.zip::https://az764295.vo.msecnd.net/stable/$_release/VSCode-linux-ia32-stable.zip
              ${pkgname}.desktop
              )
md5sums_x86_64=('4fcac208668193c80d1eb167f6ccc6be'
                'd1d9b35d20de511be44b686b0178874a')
md5sums_i686=('fb8f777bbbb244ea469808db628a878a'
              'd1d9b35d20de511be44b686b0178874a')
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

  rm -f "${srcdir}"/${pkgname}.desktop
  rm -f "${srcdir}"/${_pkg}.zip
  
  cp -r "${srcdir}/${_pkg}/"* "${pkgdir}/opt/${pkgname}" -R
  ln -s /opt/${pkgname}/code "${pkgdir}"/usr/bin/visual-studio-code
}
