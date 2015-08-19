# Maintainer: Christoph Bayer <chrbayer@chriby.de>
# Contributor: Jakub Schmidtke <sjakub-at-gmail-dot-com>
# Contributor: Figo.zhang <figo1802@gmail.com>

_rev=r01
_ver=23
pkgname=android-docs
pkgver=${_ver}_${_rev}
pkgrel=1
pkgdesc='API docs for Google Android SDK'
arch=('any')
url="http://developer.android.com"
license=('Apache')
options=(!strip)
source=("http://dl-ssl.google.com/android/repository/docs-${_ver}_${_rev}.zip")
sha1sums=('060ebab2f74861e1ddd9136df26b837312bc087f')

package() {
  mkdir -p "${pkgdir}/opt/android-sdk/"
  mv "${srcdir}/docs" "${pkgdir}/opt/android-sdk/"

  chmod -R ugo+rX "${pkgdir}/opt"
}
