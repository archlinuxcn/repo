# Maintainer: Muflone http://www.muflone.com/contacts/english/
# Contributor: navigaid <navigaid@gmail.com>

pkgname=android-apktool
pkgver=2.11.1
pkgrel=1
pkgdesc="a tool for reengineering Android apk files"
arch=('any')
url="https://github.com/iBotPeaches/Apktool"
license=('Apache-2.0')
depends=('java-runtime')
makedepends=('java-environment' 'gradle')
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/iBotPeaches/Apktool/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('1c1ac3add61c5d9043b5efdb228fbd2be7c3bd329bb6ed82228eedacef90bcb9')

build() {
  cd "Apktool-${pkgver}"
  gradle build --no-daemon shadowJar proguard
}

package() {
  cd "Apktool-${pkgver}"
  install -D -m 644 "brut.apktool/apktool-cli/build/libs/apktool-cli.jar" "${pkgdir}/usr/share/${pkgname}/apktool.jar"
  install -D -m 755 "scripts/linux/apktool" "${pkgdir}/usr/share/${pkgname}/apktool"
  install -d -m 755 "${pkgdir}/usr/bin"
  ln -s "/usr/share/${pkgname}/apktool" "${pkgdir}/usr/bin/apktool"
}

