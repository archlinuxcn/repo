# Maintainer: TTsdzb <ttsdzb at outlook dot com>
# Maintainer: Jia Yin<yenfeng.shetiko at gmail dot com>
# Contributor: Misaka13514 <Misaka13514 at gmail dot com>
# Contributor: Hao Long <imlonghao@archlinuxcn.org>
# Contributor: Lin Ruoshui <LinRs at users.noreply.github dot com>
# Contributor: hexchain <i at hexchain.org>
# Contributor: Rowisi < nomail <at> private <dot> com >
# Contributor: So1ar <so1ar114514@gmail.com>
# Contributor: Bot-wxt1221 <3264117476@qq.com>

pkgname=hmcl-bin
pkgver=3.12.4
pkgrel=6
install=.install
pkgdesc="A Minecraft Launcher which is multi-functional, cross-platform and popular."
arch=('any')
url="https://github.com/huanghongxun/HMCL"
license=('GPL-3.0-or-later')
depends=('java-runtime' 'hicolor-icon-theme')
provides=('hmcl')
conflicts=('hmcl')
replaces=('hmcl-stable-bin')
source=("hmcl.desktop"
        "hmcl-launch-script"
        "${pkgname}-${pkgver}-${pkgrel}.jar::https://github.com/HMCL-dev/HMCL/releases/download/v${pkgver}/HMCL-${pkgver}.jar"
        "icon.png::https://raw.githubusercontent.com/HMCL-dev/HMCL/main/HMCL/src/main/resources/assets/img/icon.png"
        "icon@2x.png::https://raw.githubusercontent.com/HMCL-dev/HMCL/main/HMCL/src/main/resources/assets/img/icon@2x.png"
        "icon@4x.png::https://raw.githubusercontent.com/HMCL-dev/HMCL/main/HMCL/src/main/resources/assets/img/icon@4x.png"
        "icon@8x.png::https://raw.githubusercontent.com/HMCL-dev/HMCL/main/HMCL/src/main/resources/assets/img/icon@8x.png")
sha256sums=('9a561081f8f3ece3da114afd4f6d90565ca0e04716eef4ea88c6b4306566ae9b'
            'fe8c663bd3aaee7c70dff4da75781a078993c665e5492883d708e46658e6c0ec'
            '0b12ecdeb316fbe14617b595f443086feebd66b9d5d8c69d1070ff34cc97048c'
            '8fcf46efaa5e7e1ecde943b11cb65ae7c827933699d0274df4382421b19af054'
            '16ad1c9d42db302aa745fb343ab935dc51c0640e39be50e0095ebfc6036816b6'
            '3ab644efc6d2765cfcb9bb3833548d45d0d6aeba8b7da1dd08c70db267d6dfdb'
            '37a6b52938af13a4eaa8c045f9bc19a181bb7ef49e1f6827e6bc07839d19eb33')

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
