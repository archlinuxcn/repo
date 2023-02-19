# Maintainer: Hao Long <imlonghao@archlinuxcn.org>
# Contributor: Lin Ruoshui <LinRs at users.noreply.github dot com>
# Contributor: hexchain <i at hexchain.org>

pkgname=hmcl
_pkgname=HMCL
pkgver=3.5.4
_commit=5fa066de6b08e348b8d13294c0695d80749f241a
pkgrel=1
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
b2sums=('1de8eca922b01b9c4c6d9a173143f05b900fd6b12b1b27bae175948a43125619d0e14c82d704548f70539af13eb4fd9f7288749265949089c7d6a8fe9032d284'
        '6c38da38fa13ad0af061d593f7733d6a406025c473240ccee4d07c89e71f8d5ead430374a7500f1395a7341c67e06ef3664cb1747ab93cba63459f7906b1598a'
        '90eb3597f8f359ebfef6f65f88ee85bfa55212131772dd566041cba311a2f29295f28bee569b10e5c4afef102ace531da2f13cab74191d5dae6566c36522378d')

build() {
  cd "${_pkgname}-${_commit}"
  export JAVA_HOME=/usr/lib/jvm/liberica-jdk-11-full
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
