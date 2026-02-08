# Maintainer: TTsdzb <ttsdzb at outlook dot com>
# Maintainer: Jia Yin<yenfeng.shetiko at gmail dot com>

pkgname=hmcl-beta-bin
pkgver=3.11.0.325
pkgrel=1
pkgdesc="A Minecraft Launcher which is multi-functional, cross-platform and popular."
arch=('any')
url="https://github.com/huanghongxun/HMCL"
license=('GPL-3.0-or-later')
depends=('java-runtime' 'hicolor-icon-theme')
provides=('hmcl')
conflicts=('hmcl')
source=("hmcl.desktop"
        "hmcl-launch-script"
        "${pkgname}-${pkgver}-${pkgrel}.jar::https://github.com/HMCL-dev/HMCL/releases/download/v${pkgver}/HMCL-${pkgver}.jar")
sha256sums=('ef5edb4285293c77162374e15f01f3540c7f511f6d9ab5b7244c4b01eb8512de'
            '296914106dac2d07c9ce2bc92a91568830534332e9bf7554ea591f22efa357df'
            '376353d59ce6cef56323ac0c4166dfc58eb30a08a6a83e6db9cb5514626ed084')

noextract=("${pkgname}-${pkgver}-${pkgrel}.jar")

prepare() {
  # extract icons from jar
  # Thanks to @Misaka13514
  local _iconfile
  for _iconfile in icon.png icon@2x.png icon@4x.png icon@8x.png; do
    jar -xf "${pkgname}-${pkgver}-${pkgrel}.jar" "assets/img/${_iconfile}"
  done
}

package() {
  install -Dm644 "${pkgname}-${pkgver}-${pkgrel}.jar" "${pkgdir}/usr/share/java/${pkgname}/${pkgname}.jar"
  install -Dm755 "hmcl-launch-script" "${pkgdir}/usr/bin/${pkgname}"
  install -Dm644 "hmcl.desktop" "${pkgdir}/usr/share/applications/${pkgname}.desktop"

  # install icons
  local _icon _iconfile
  for _icon in 32:icon.png 64:icon@2x.png 128:icon@4x.png 256:icon@8x.png; do
    _iconfile=${_icon#*:}
    _icon=${_icon%:*}
    install -Dm644 "assets/img/${_iconfile}" "${pkgdir}/usr/share/icons/hicolor/${_icon}x${_icon}/apps/${pkgname}.png"
  done
}
