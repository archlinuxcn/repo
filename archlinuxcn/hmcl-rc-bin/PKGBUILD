# Maintainer: TTsdzb <ttsdzb at outlook dot com>
# Maintainer: Jia Yin<yenfeng.shetiko at gmail dot com>

pkgname=hmcl-rc-bin
pkgver=3.10.3
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
sha256sums=('904999db15ae0094dc364913f4aa14f500626bb6b50a37cc8c2090bb9f6ae385'
            'b11eca896b79e206a6991e82b82fb1e9a2a1e3e5ce04757114a37747213a76ab'
            'fb1c430026b61026d66825332b46ffadc452e3d1dec781990dc34d2bf684511b')

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
