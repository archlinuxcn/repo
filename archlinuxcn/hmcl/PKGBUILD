# Maintainer: Hao Long <imlonghao@archlinuxcn.org>
# Contributor: Lin Ruoshui <LinRs at users.noreply.github dot com>
# Contributor: hexchain <i at hexchain.org>

pkgname=hmcl
_pkgname=HMCL
pkgver=3.3.188
_commit=447afaa76f111936a10f54c884bab5129c50f409
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
sha256sums=('b9e66ecda49285fb076f2c383420854b639c56e4bb240e86dbf666f5929dc1a5'
            '5780cf70f1afec0eb3cd8fc43297d361903c7204e274a28c5edf9b8ac3eea83e'
            'ac4d57b9c662e1672240ca9b362b64670098a25569f6e6722634424d7fb2f5fc')

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
