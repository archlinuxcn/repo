# Maintainer: Muflone http://www.muflone.com/contacts/english/
# Contributor: navigaid <navigaid@gmail.com>

pkgname=android-apktool
pkgver=2.8.1
pkgrel=2
pkgdesc="a tool for reengineering Android apk files"
arch=('any')
url="https://github.com/iBotPeaches/Apktool"
license=('Apache')
depends=('java-runtime')
makedepends=('java-environment' 'gradle')
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/iBotPeaches/Apktool/archive/refs/tags/v${pkgver}.tar.gz"
        "http://connortumbleson.com/apktool/googlecode/apktool-install-linux-r04-brut1.tar.bz2")
sha256sums=('6ca40ed788091c9525e98b9734d5b2f0bb1bc0db786884ca805e1d37f6e989f5'
            'cffa5c0a46bab9c66da02cc5db651c3a8321bee98580815e44c802d62a696dfa')

prepare() {
  sed -i 's/libdir=.*progdir/libdir="\/usr\/share\/'${pkgname}'/' apktool
}

build() {
  cd "Apktool-${pkgver}"
  gradle build --no-daemon
}

package() {
  cd "Apktool-${pkgver}"
  install -Dm 0755 "${srcdir}/apktool" "${pkgdir}/usr/bin/apktool"
  install -Dm 0644 "brut.apktool/apktool-cli/build/libs/apktool-cli-all.jar" "${pkgdir}/usr/share/${pkgname}/apktool.jar"
}
