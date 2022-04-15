# Maintainer: Hao Long <imlonghao@archlinuxcn.org>
# Contributor: Lin Ruoshui <LinRs at users.noreply.github dot com>
# Contributor: hexchain <i at hexchain.org>

pkgname=hmcl
_pkgname=HMCL
pkgver=3.5.3
_commit=d28723916d6d42fbea2a6423a07a74ffdf7cd1bd
pkgrel=2
pkgdesc="A Minecraft Launcher which is multi-functional, cross-platform and popular"
arch=('any')
url="https://github.com/huanghongxun/HMCL"
license=('GPL3')
provides=('hmcl')
conflicts=('hmcl')
depends=('java-runtime')
makedepends=('liberica-jdk-11-full-bin')
source=("hmcl-launch-script"
        "${pkgname}.desktop"
        "${pkgname}-${pkgver}.tgz::${url}/archive/${_commit}.tar.gz")
b2sums=('f18bf46c0f766faa54db83fffde98273d3917a62890f6a118be834d753405159b4afe851ee94023cc97d32ad97900015b65d1ad7fcb12935d3c6b047d9292271'
        '6c38da38fa13ad0af061d593f7733d6a406025c473240ccee4d07c89e71f8d5ead430374a7500f1395a7341c67e06ef3664cb1747ab93cba63459f7906b1598a'
        '24f676aa10d7865f079eb155b44790c344415f1cfcc43ab4dd0ad4f9c408c2b6c622b2d24090fd3eca6bb14f04e19087b56bbb757bfe8b639d1eec20cc00c927')

build() {
  cd "${_pkgname}-${_commit}"
  ./gradlew clean build
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
