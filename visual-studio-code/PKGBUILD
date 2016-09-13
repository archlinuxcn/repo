# Maintainer: D. Can Celasun <dcelasun[at]gmail[dot]com>

pkgname=visual-studio-code
pkgver=1.5.2
pkgrel=1
pkgdesc="Editor for building and debugging modern web and cloud applications"
arch=('x86_64' 'i686')
url="https://code.visualstudio.com/"
license=('custom: commercial')
provides=('vscode','visualstudiocode')
depends=(fontconfig libxtst gtk2 python cairo alsa-lib gconf nss gcc-libs libnotify)
_release=66f37fd2a99eb9d628dd374d81d78835b410c39b
_ts64=1473686317
_ts32=1473685537
source_x86_64=(vscode64_${pkgver}.zip::https://az764295.vo.msecnd.net/stable/$_release/code-stable-code_${pkgver}-${_ts64}_amd64.tar.gz
               ${pkgname}.desktop
               )
source_i686=(vscode32_${pkgver}.zip::https://az764295.vo.msecnd.net/stable/$_release/code-stable-code_${pkgver}-${_ts32}_i386.tar.gz
              ${pkgname}.desktop
              )
md5sums_x86_64=('356d72187479ad3c5020b35247b37463'
                '89eb024d17221e5c92c99c390eaf92ce')
md5sums_i686=('8cd38e3c20a2c1e0774adda52bdc2158'
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

  cp -r "${srcdir}/${_pkg}/"* "${pkgdir}/opt/${pkgname}" -R
  ln -s /opt/${pkgname}/bin/code "${pkgdir}"/usr/bin/code
}
