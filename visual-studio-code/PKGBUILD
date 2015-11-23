# Maintainer: D. Can Celasun <dcelasun[at]gmail[dot]com>

pkgname=visual-studio-code
pkgver=0.10.1
pkgrel=3
pkgdesc="Editor for building and debugging modern web and cloud applications"
arch=('x86_64' 'i686')
url="https://code.visualstudio.com/"
license=('custom: commercial')
provides=('vscode','visualstudiocode')
depends=(fontconfig libxtst gtk2 python cairo alsa-lib gconf nss gcc-libs)
source_x86_64=(VSCode-linux64_${pkgver}.zip::https://az764295.vo.msecnd.net/public/${pkgver}/VSCode-linux64.zip
               ${pkgname}.desktop
               )
source_i686=(VSCode-linux32_${pkgver}.zip::https://az764295.vo.msecnd.net/public/${pkgver}/VSCode-linux32.zip
              ${pkgname}.desktop
              )
md5sums_x86_64=('3d37a4b05e2457651447e0e77efac4d8'
                '94c9ab66cc24c2683873e07b2a5aada4')
md5sums_i686=('b0f120824ca51f109c4280ed6bd9e8bd'
              '94c9ab66cc24c2683873e07b2a5aada4')
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
  install -m644 "${srcdir}/${_pkg}/resources/app/resources/linux/vscode.png" "${pkgdir}/usr/share/icons/${pkgname}.png"
  install -m644 "${srcdir}/${pkgname}.desktop" "${pkgdir}/usr/share/applications/${pkgname}.desktop"

  rm -f "${srcdir}"/${pkgname}.desktop
  rm -f "${srcdir}"/${_pkg}.zip
  
  cp -r "${srcdir}/${_pkg}/"* "${pkgdir}/opt/${pkgname}" -R
  ln -s /opt/${pkgname}/Code "${pkgdir}"/usr/bin/visual-studio-code
}
