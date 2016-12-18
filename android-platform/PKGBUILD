# Maintainers: goetzc
# Contributors: lestb, Philipp Wolfer, Joel Pedraza, Jakub Schmidtke
# Package Repository: https://github.com/mij-aur-packages/android-platform

pkgname=android-platform
_apilevel=25
_rev=r03
pkgver=${_apilevel}_${_rev}
pkgrel=1
pkgdesc="Android SDK Platform, latest API"
arch=('any')
url="http://developer.android.com/sdk/index.html"
license=('custom')
depends=('android-sdk' 'android-sdk-platform-tools')
provides=("${pkgname}-${_apilevel}")
conflicts=("${pkgname}-${_apilevel}")
options=('!strip')
source=("https://dl-ssl.google.com/android/repository/platform-${_apilevel}_${_rev}.zip")
sha1sums=('00c2c5765e8988504be10a1eb66ed71fcdbd7fe8')

package() {
  mkdir -p "${pkgdir}/opt/android-sdk/platforms/"
  find "${srcdir}" -maxdepth 1 -mindepth 1 -type d | grep -P 'android-[0-9]+(\.[0-9]*)*$' | while read directory; do
      mv "${directory}" "${pkgdir}/opt/android-sdk/platforms/android-${_apilevel}"
  done

  chmod -R ugo+rX "${pkgdir}/opt"
}
