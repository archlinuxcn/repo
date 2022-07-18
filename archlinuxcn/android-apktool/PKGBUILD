# Maintainer: Muflone http://www.muflone.com/contacts/english/
# Contributor: navigaid <navigaid@gmail.com>

pkgname=android-apktool
pkgver=2.6.1
pkgrel=1
pkgdesc="a tool for reengineering Android apk files"
arch=('any')
url="http://forum.xda-developers.com/showthread.php?t=1755243"
license=('Apache')
depends=('java-runtime')
source=("https://github.com/iBotPeaches/Apktool/releases/download/v${pkgver}/apktool_${pkgver}.jar"
        "http://connortumbleson.com/apktool/googlecode/apktool-install-linux-r04-brut1.tar.bz2")
sha256sums=('bc2b9a87ac5a86905b6ca343c21a0db3bc37bdd51154bc9cdf65523d95895d34'
            'cffa5c0a46bab9c66da02cc5db651c3a8321bee98580815e44c802d62a696dfa')

prepare() {
  sed -i 's/libdir=.*progdir/libdir="\/usr\/share\/'${pkgname}'/' apktool
}

package() {
  install -Dm 0755 "${srcdir}/apktool" "${pkgdir}/usr/bin/apktool"
  install -Dm 0644 "${srcdir}/apktool_${pkgver}.jar" "${pkgdir}/usr/share/${pkgname}/apktool.jar"
}
