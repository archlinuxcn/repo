# Maintainers: goetzc
# Contributors: lestb, Philipp Wolfer, Joel Pedraza, Jakub Schmidtke
# Package Repository: https://github.com/mij-aur-packages/android-platform

pkgname=android-platform
_apilevel=26
_rev=r02
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
sha512sums=('7f125570e0e2e347865503148af23f9f6402456e5afe724ac19f788c4fbc3ae7c1305707502f87206e8a9bb7b720ac383a881f411586f3d0fff913273e7cb961')

package() {
  mkdir -p "${pkgdir}/opt/android-sdk/platforms/"
  find "${srcdir}" -maxdepth 1 -mindepth 1 -type d | grep -P 'android-[0-9]+(\.[0-9]*)*$' | while read directory; do
      mv "${directory}" "${pkgdir}/opt/android-sdk/platforms/android-${_apilevel}"
  done

  chmod -R ugo+rX "${pkgdir}/opt"
}
