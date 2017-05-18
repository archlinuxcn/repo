# Maintainer: Sandor Nagy <sandor-dot-nagy-at-kdemail-dot-net>
# Contributor: Jakub Schmidtke <sjakub-at-gmail-dot-com>

pkgname=android-support
pkgver=r23.2.1
pkgrel=1
pkgdesc='Android Support Package'
arch=('any')
url="https://developer.android.com/sdk/compatibility-library.html"
license=('custom')
depends=('android-sdk')
options=('!strip')
source=("http://dl-ssl.google.com/android/repository/support_${pkgver}.zip" 'source.properties')
sha1sums=('41121bbc412c2fce0be170d589d20cfa3e78e857'
          '43f89b499226845fccb75bd3deab57fb16a18153')

package() {
  mkdir -p "${pkgdir}/opt/android-sdk/extras/android/"
  mv "${srcdir}/support" "${pkgdir}/opt/android-sdk/extras/android/support"

  chmod -R ugo+rX "${pkgdir}/opt"
  install -Dm644 "${srcdir}/source.properties" "${pkgdir}/opt/android-sdk/extras/android/support/source.properties"
}
