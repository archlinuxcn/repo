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
pkgver=3.10.2
pkgrel=3
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
        "${pkgname}-${pkgver}-${pkgrel}.jar::https://github.com/HMCL-dev/HMCL/releases/download/v${pkgver}/HMCL-${pkgver}.jar")
sha256sums=('9a561081f8f3ece3da114afd4f6d90565ca0e04716eef4ea88c6b4306566ae9b'
            'fe8c663bd3aaee7c70dff4da75781a078993c665e5492883d708e46658e6c0ec'
            'b6640dd244a39bca14dfa10d1e1800eb8f48a21746e190c7c8468c3ec71dde74')

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
