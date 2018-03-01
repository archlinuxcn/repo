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
sha384sums=('da778b2688355151e55fc1fe7763b67c087470c2afd1122007c04d58153c27bdcd5bb4ee0ca423e4e84bad243a87b95b')

package() {
  mkdir -p "${pkgdir}/opt/android-sdk/platforms/"
  find "${srcdir}" -maxdepth 1 -mindepth 1 -type d | grep -P 'android-[0-9]+(\.[0-9]*)*$' | while read directory; do
      mv "${directory}" "${pkgdir}/opt/android-sdk/platforms/android-${_apilevel}"
  done

  chmod -R ugo+rX "${pkgdir}/opt"
}
