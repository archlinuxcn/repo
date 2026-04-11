# Maintainer: TTsdzb <ttsdzb at outlook dot com>
# Maintainer: Jia Yin<yenfeng.shetiko at gmail dot com>

pkgname=hmcl-beta-bin
pkgver=3.13.0.340
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
        "${pkgname}-${pkgver}-${pkgrel}.jar::https://github.com/HMCL-dev/HMCL/releases/download/v${pkgver}/HMCL-${pkgver}.jar"
        "${pkgname}-${pkgver}-${pkgrel}.png::https://raw.githubusercontent.com/HMCL-dev/HMCL/v${pkgver}/HMCL/src/main/resources/assets/img/icon.png"
        "${pkgname}-${pkgver}-${pkgrel}@2x.png::https://raw.githubusercontent.com/HMCL-dev/HMCL/v${pkgver}/HMCL/src/main/resources/assets/img/icon@2x.png"
        "${pkgname}-${pkgver}-${pkgrel}@4x.png::https://raw.githubusercontent.com/HMCL-dev/HMCL/v${pkgver}/HMCL/src/main/resources/assets/img/icon@4x.png"
	"${pkgname}-${pkgver}-${pkgrel}@8x.png::https://raw.githubusercontent.com/HMCL-dev/HMCL/v${pkgver}/HMCL/src/main/resources/assets/img/icon@8x.png")
sha256sums=('ef5edb4285293c77162374e15f01f3540c7f511f6d9ab5b7244c4b01eb8512de'
            '296914106dac2d07c9ce2bc92a91568830534332e9bf7554ea591f22efa357df'
            '1c7fa624ba758b3337c38bef36f38e3fddd0035efee8d1bd1ebd3bbd8b16595a'
            '44c6ac6aa2c55c35826f873dfd3dbf11cb7675f2e88040c64bdea861426aa861'
            '592f4c5bcf636250e6d4cad6b6a45bb49fd01cb346072b1dc9b7ff703fd26fce'
            '91a67409bb46a5105eb713956e4061621b7a4542ef0de52952287a995993c6d0'
            'd4e56ae2e8c0d991dba01ef3124ef4d38918825f58728338a8bab5e78319306a')

noextract=("${pkgname}-${pkgver}-${pkgrel}.jar")

package() {
  install -Dm644 "${pkgname}-${pkgver}-${pkgrel}.jar" "${pkgdir}/usr/share/java/${pkgname}/${pkgname}.jar"
  install -Dm755 "hmcl-launch-script" "${pkgdir}/usr/bin/${pkgname}"
  install -Dm644 "hmcl.desktop" "${pkgdir}/usr/share/applications/${pkgname}.desktop"

  # install icons
  local _icon _iconfile
  for _icon in 32:${pkgname}-${pkgver}-${pkgrel}.png 64:${pkgname}-${pkgver}-${pkgrel}@2x.png 128:${pkgname}-${pkgver}-${pkgrel}@4x.png 256:${pkgname}-${pkgver}-${pkgrel}@8x.png; do
    _iconfile=${_icon#*:}
    _icon=${_icon%:*}
    install -Dm644 "${_iconfile}" "${pkgdir}/usr/share/icons/hicolor/${_icon}x${_icon}/apps/${pkgname}.png"
  done
}
