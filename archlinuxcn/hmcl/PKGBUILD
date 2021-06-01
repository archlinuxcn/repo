# Maintainer: Hao Long <imlonghao@archlinuxcn.org>
# Contributor: Lin Ruoshui <LinRs at users.noreply.github dot com>
# Contributor: hexchain <i at hexchain.org>

pkgname=hmcl
_pkgname=HMCL
pkgver=3.3.172
_commit=bd18355a1a02a8f6a927edd7dadadbf18857e6e9
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
sha256sums=('5565dafda05a2f15e6d6c58aedc3a4c9191fa2f165796c9d9fc32fdf5efa1ab2'
            '5780cf70f1afec0eb3cd8fc43297d361903c7204e274a28c5edf9b8ac3eea83e'
            'e8e092205541e142b3d31975afc89330fb27b1d367f90d5a66758b1b08816290')

prepare() {
  cd "${_pkgname}-${_commit}"
  # Fix license check
  sed "s/\${year}/2020/" license-header.txt -i
}

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
