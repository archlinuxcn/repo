# Maintainer: TTsdzb <ttsdzb at outlook dot com>
# Maintainer: Jia Yin<yenfeng.shetiko at gmail dot com>

pkgname=hmcl-beta-bin
pkgver=3.13.0.339
pkgrel=3
pkgdesc="A Minecraft Launcher which is multi-functional, cross-platform and popular."
arch=('any')
url="https://github.com/huanghongxun/HMCL"
license=('GPL-3.0-or-later')
depends=('java-runtime' 'hicolor-icon-theme')
provides=('hmcl')
conflicts=('hmcl')
source=("hmcl.desktop"
        "hmcl-launch-script"
        "${pkgname}-${pkgver}-${pkgrel}.jar::https://github.com/HMCL-dev/HMCL/releases/download/v${pkgver}/HMCL-${pkgver}.jar"
        "icon.png::https://github.com/HMCL-dev/HMCL/blob/main/HMCL/src/main/resources/assets/img/icon.png"
        "icon@2x.png::https://github.com/HMCL-dev/HMCL/blob/main/HMCL/src/main/resources/assets/img/icon@2x.png"
        "icon@4x.png::https://github.com/HMCL-dev/HMCL/blob/main/HMCL/src/main/resources/assets/img/icon@4x.png"
        "icon@8x.png::https://github.com/HMCL-dev/HMCL/blob/main/HMCL/src/main/resources/assets/img/icon@8x.png")
sha256sums=('ef5edb4285293c77162374e15f01f3540c7f511f6d9ab5b7244c4b01eb8512de'
            '296914106dac2d07c9ce2bc92a91568830534332e9bf7554ea591f22efa357df'
            '9ba8de88261fab281ba017c5596b63bb871c6ef029981c557673b0b6aec0d2ce'
            'dfdb316c25f8c6f1329b095ca84ee842680451f0ae061c3cac7b97d6129f9348'
            'ca7bbdd406643d82a97fccd2a50d35f71f8f37b55907d8a816981177add0b99b'
            '6bdcccd199d0475e8c937f46f211e3a2b22722c8fc2c00e2704e08447feec0cb'
            '3d280c9f1ebcfd7407426f98cd988ab5729c4a12f14f83b67c9e4d2bdb5ace38')

noextract=("${pkgname}-${pkgver}-${pkgrel}.jar")

package() {
  install -Dm644 "${pkgname}-${pkgver}-${pkgrel}.jar" "${pkgdir}/usr/share/java/${pkgname}/${pkgname}.jar"
  install -Dm755 "hmcl-launch-script" "${pkgdir}/usr/bin/${pkgname}"
  install -Dm644 "hmcl.desktop" "${pkgdir}/usr/share/applications/${pkgname}.desktop"

  # install icons
  local _icon _iconfile
  for _icon in 32:icon.png 64:icon@2x.png 128:icon@4x.png 256:icon@8x.png; do
    _iconfile=${_icon#*:}
    _icon=${_icon%:*}
    install -Dm644 "${_iconfile}" "${pkgdir}/usr/share/icons/hicolor/${_icon}x${_icon}/apps/${pkgname}.png"
  done
}
