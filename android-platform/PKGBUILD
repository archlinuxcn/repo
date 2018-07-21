# Maintainers: goetzc
# Contributors: lestb, Philipp Wolfer, Joel Pedraza, Jakub Schmidtke
# Package Repository: https://github.com/mij-aur-packages/android-platform

pkgname=android-platform
_apilevel=27
_rev=r01
pkgver=${_apilevel}_${_rev}
pkgrel=2
pkgdesc="Android SDK Platform, latest API"
arch=('any')
url="http://developer.android.com/sdk/index.html"
license=('custom')
depends=('android-sdk' 'android-sdk-platform-tools')
provides=("${pkgname}-${_apilevel}")
conflicts=("${pkgname}-${_apilevel}")
options=('!strip')
source=("https://dl-ssl.google.com/android/repository/platform-${_apilevel}_${_rev}.zip")
sha384sums=('269d9373d55f0f93994401b9d733e98b599d42c680d6d4436a91232024c298bc1e3d717288f94f85c303b2c2c93e8dc5')

package() {
  mkdir -p "${pkgdir}/opt/android-sdk/platforms/"
  find "${srcdir}" -maxdepth 1 -mindepth 1 -type d | grep -P 'android-[0-9]+(\.[0-9]*)*$' | while read directory; do
      mv "${directory}" "${pkgdir}/opt/android-sdk/platforms/android-${_apilevel}"
  done

  chmod -R ugo+rX "${pkgdir}/opt"
}
