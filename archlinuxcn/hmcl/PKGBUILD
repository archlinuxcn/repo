# Maintainer: Misaka13514 <Misaka13514 at gmail dot com>
# Contributor: Hao Long <imlonghao@archlinuxcn.org>
# Contributor: Lin Ruoshui <LinRs at users.noreply.github dot com>
# Contributor: hexchain <i at hexchain.org>

pkgname=hmcl
_pkgname=HMCL
pkgver=3.6.17
_tag="release-${pkgver}"
pkgrel=1
pkgdesc="A Minecraft Launcher which is multi-functional, cross-platform and popular"
arch=('any')
url="https://github.com/HMCL-dev/HMCL"
license=('GPL-3.0-or-later')
depends=('java-runtime' 'hicolor-icon-theme')
makedepends=('java-environment-openjdk=11')
install="$pkgname.install"
source=("hmcl-launch-script"
        "${pkgname}.desktop"
        "${pkgname}-${pkgver}.tgz::${url}/archive/${_tag}.tar.gz")
b2sums=('1de8eca922b01b9c4c6d9a173143f05b900fd6b12b1b27bae175948a43125619d0e14c82d704548f70539af13eb4fd9f7288749265949089c7d6a8fe9032d284'
        '6c38da38fa13ad0af061d593f7733d6a406025c473240ccee4d07c89e71f8d5ead430374a7500f1395a7341c67e06ef3664cb1747ab93cba63459f7906b1598a'
        'dc6347fb426cc0b113333b528245fa159cb9f7b4e59b7aa122a65a222383b496e43cdb1f69b0a091477c632defbbc916a548f73655cce1063565b228617003f1')

build() {
  # Pre-configured Microsoft Azure app credentials for HMCL's Microsoft login feature
  # These are maintained by the package maintainer (Misaka13514) to ensure out-of-box
  # functionality for users who cannot register their own Azure application

  # Registration guide:
  # https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app
  # https://help.minecraft.net/hc/en-us/articles/16254801392141
  export MICROSOFT_AUTH_ID='004be3ca-1c2a-4dc1-b805-d06494b3e968'
  export MICROSOFT_AUTH_SECRET='~mD8Q~J1C4cwiiEoTUdR3XYA96Jobsp.EZEnCauP'

  cd "${_pkgname}-${_tag}"
  export JAVA_HOME=/usr/lib/jvm/java-11-openjdk
  ./gradlew clean build --no-daemon
}

package() {
  # custom launch script
  install -Dm755 "hmcl-launch-script" "${pkgdir}/usr/bin/$pkgname"
  # desktop file
  install -Dm644 "hmcl.desktop" "${pkgdir}/usr/share/applications/${pkgname}.desktop"

  cd "${_pkgname}-${_tag}/${_pkgname}/build"

  # install jar
  _path=$(echo libs/HMCL*.jar)
  install -Dm644 $_path "${pkgdir}/usr/share/java/${pkgname}/${pkgname}.jar"
  # install icons
  local _icon _iconfile
  for _icon in 32:icon.png 64:icon@2x.png 128:icon@4x.png 256:icon@8x.png; do
    _iconfile=${_icon#*:}
    _icon=${_icon%:*}
    install -Dm644 "resources/main/assets/img/${_iconfile}" "${pkgdir}/usr/share/icons/hicolor/${_icon}x${_icon}/apps/${pkgname}.png"
  done
}
