# Maintainer: Fredy García <frealgagu at gmail dot com>

pkgname=whatsapp-nativefier
pkgver=0.3.1846
pkgrel=1
pkgdesc="WhatsApp desktop built with nativefier (electron)"
arch=("armv7l" "i686" "x86_64")
url="https://web.${pkgname%-nativefier}.com"
license=("custom")
depends=("gtk3" "libxss" "nss")
makedepends=("imagemagick" "nodejs-nativefier")
source=("${pkgname}.png"
        "${pkgname}.desktop"
        "${pkgname}-inject.js")
sha256sums=("3899581abcfed9b40b7208bbbca8bdbfe3ae9655980dbf55f04dec9cb3309f27"
            "a4ea20639ea570d2f9ec6040b8873136fa507e0aa2341fd98aad25aa6bb66e2e"
            "043bd3f16d42464fab92d9ecd9ca4312f9a2bc07ca4da106df73ae0f227fa67f")

build() {
  cd "${srcdir}"
  
  nativefier \
    --name "WhatsApp" \
    --icon "${pkgname}.png" \
    --width "800px" \
    --height "600px" \
    --inject "${pkgname}-inject.js" \
    --verbose \
    --tray \
    "https://web.${pkgname%-nativefier}.com"
}

package() {
  install -dm755 "${pkgdir}/"{opt,usr/{bin,share/{applications,licenses/${pkgname}}}}

  cp -rL "${srcdir}/whats-app-linux-"* "${pkgdir}/opt/${pkgname}"
  ln -s "/opt/${pkgname}/whats-app" "${pkgdir}/usr/bin/${pkgname}"
  install -Dm755 "${srcdir}/${pkgname}.desktop" "${pkgdir}/usr/share/applications/${pkgname}.desktop"
  install -Dm755 "${pkgdir}/opt/${pkgname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  for _size in "192x192" "128x128" "96x96" "64x64" "48x48" "32x32" "24x24" "22x22" "20x20" "16x16" "8x8"
  do
    install -dm755 "${pkgdir}/usr/share/icons/hicolor/${_size}/apps"
    convert "${srcdir}/${pkgname}.png" -resize "${_size}" "${pkgdir}/usr/share/icons/hicolor/${_size}/apps/${pkgname}.png"
  done
}

