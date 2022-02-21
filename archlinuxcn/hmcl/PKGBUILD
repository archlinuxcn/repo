# Maintainer: Hao Long <imlonghao@archlinuxcn.org>
# Contributor: Lin Ruoshui <LinRs at users.noreply.github dot com>
# Contributor: hexchain <i at hexchain.org>

pkgname=hmcl
_pkgname=HMCL
pkgver=3.5.3
_commit=d28723916d6d42fbea2a6423a07a74ffdf7cd1bd
pkgrel=1
pkgdesc="A Minecraft Launcher which is multi-functional, cross-platform and popular"
arch=('any')
url="https://github.com/huanghongxun/HMCL"
license=('GPL3')
provides=('hmcl')
conflicts=('hmcl')
depends=('java8-openjfx'
         'jdk8-openjdk')
source=("hmcl-launch-script"
        "${pkgname}.desktop"
        "${pkgname}-${pkgver}.tgz::${url}/archive/${_commit}.tar.gz")
b2sums=('ed19ac232f25c09bd468e6932e97ff406608b64aac337f666d7702f047778e17170054ae5e3b6de8ad2f947c1edab8cd9eb8b1b4886597562137e568ddf3c1de'
        '6c38da38fa13ad0af061d593f7733d6a406025c473240ccee4d07c89e71f8d5ead430374a7500f1395a7341c67e06ef3664cb1747ab93cba63459f7906b1598a'
        '24f676aa10d7865f079eb155b44790c344415f1cfcc43ab4dd0ad4f9c408c2b6c622b2d24090fd3eca6bb14f04e19087b56bbb757bfe8b639d1eec20cc00c927')

build() {
  cd "${_pkgname}-${_commit}"
  _java=$(ls /usr/lib/jvm | grep 8-openjdk)
  export JAVA_HOME=/usr/lib/jvm/$_java
  sh gradlew build
}

package() {
  # custom launch script
  install -Dm755 "hmcl-launch-script" "${pkgdir}/usr/bin/$pkgname"
  # desktop file
  install -Dm644 "hmcl.desktop" "${pkgdir}/usr/share/applications/${pkgname}.desktop"

  cd "${_pkgname}-${_commit}/${_pkgname}/build"

  # install jar
  _path=$(echo libs/HMCL*.jar)
  install -Dm644 $_path "${pkgdir}/usr/share/java/${pkgname}/${pkgname}.jar"
  # install icon
  install -Dm644 "resources/main/assets/img/craft_table.png" "${pkgdir}/usr/share/icons/hicolor/48x48/apps/${pkgname}.png"
}
