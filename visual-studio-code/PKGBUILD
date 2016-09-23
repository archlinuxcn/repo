# Maintainer: D. Can Celasun <dcelasun[at]gmail[dot]com>

pkgname=visual-studio-code
pkgver=1.5.3
pkgrel=1
pkgdesc="Editor for building and debugging modern web and cloud applications"
arch=('x86_64' 'i686')
url="https://code.visualstudio.com/"
license=('custom: commercial')
provides=('vscode','visualstudiocode')
depends=(fontconfig libxtst gtk2 python cairo alsa-lib gconf nss gcc-libs libnotify)
_release=5be4091987a98e3870d89d630eb87be6d9bafd27
_ts64=1474533365
_ts32=1474534134
source_x86_64=(vscode64_${pkgver}.zip::https://az764295.vo.msecnd.net/stable/$_release/code-stable-code_${pkgver}-${_ts64}_amd64.tar.gz
               ${pkgname}.desktop
               )
source_i686=(vscode32_${pkgver}.zip::https://az764295.vo.msecnd.net/stable/$_release/code-stable-code_${pkgver}-${_ts32}_i386.tar.gz
              ${pkgname}.desktop
              )
md5sums_x86_64=('e564b2d717b0481ae100ad5f8d81e05d'
                '89eb024d17221e5c92c99c390eaf92ce')
md5sums_i686=('3003500c128ed229e0be9683433f2984'
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
