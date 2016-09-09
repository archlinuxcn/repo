# Maintainer: D. Can Celasun <dcelasun[at]gmail[dot]com>

pkgname=visual-studio-code
pkgver=1.5.0
pkgrel=1
pkgdesc="Editor for building and debugging modern web and cloud applications"
arch=('x86_64' 'i686')
url="https://code.visualstudio.com/"
license=('custom: commercial')
provides=('vscode','visualstudiocode')
depends=(fontconfig libxtst gtk2 python cairo alsa-lib gconf nss gcc-libs libnotify)
_release=4fc690be310dd02e0ab6529c0b9bf348a8b26a19
_ts64=1473324851
_ts32=1473325631
source_x86_64=(vscode64_${pkgver}.zip::https://az764295.vo.msecnd.net/stable/$_release/code-stable-code_${pkgver}-${_ts64}_amd64.tar.gz
               ${pkgname}.desktop
               )
source_i686=(vscode32_${pkgver}.zip::https://az764295.vo.msecnd.net/stable/$_release/code-stable-code_${pkgver}-${_ts32}_i386.tar.gz
              ${pkgname}.desktop
              )
md5sums_x86_64=('7b4de90d6a51f907603877cac9432cda'
                '89eb024d17221e5c92c99c390eaf92ce')
md5sums_i686=('2270dbd72ff7caa274ae9c291ba83960'
              '89eb024d17221e5c92c99c390eaf92ce')
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
  ln -s /opt/${pkgname}/bin/code "${pkgdir}"/usr/bin/code
}
