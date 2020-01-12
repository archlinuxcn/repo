# Maintainers: goetzc, Skycoder42
# Contributors: lestb, Philipp Wolfer, Joel Pedraza, Jakub Schmidtke

pkgname=android-platform
_apilevel=29
_rev=r04
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
sha1sums=('8d644c39902038e0bd529165d5ba4f5a8607daea')
sha384sums=('9308ff2278b1beafe7096985825d331977694163f2e2b69b222cc4772fb44ac3bceeeca4a009bfec045d86a552cdb3cc')

package() {
  mkdir -p "${pkgdir}/opt/android-sdk/platforms/"
  find "${srcdir}" -maxdepth 1 -mindepth 1 -type d | grep -P 'android-[0-9]+(\.[0-9]*)*$' | while read directory; do
      mv "${directory}" "${pkgdir}/opt/android-sdk/platforms/android-${_apilevel}"
  done

  chmod -R ugo+rX "${pkgdir}/opt"
}
