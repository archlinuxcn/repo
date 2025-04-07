# Maintainer: Gustavo Alvarez <sl1pkn07@gmail.com>
# Contributor: garion < garion @ mailoo.org >

pkgname=mkvalidator
pkgver=0.6.0
pkgrel=1
pkgdesc="Validator for MKV files"
arch=('x86_64')
url='https://www.matroska.org/downloads/mkvalidator.html'
license=('BSD')
depends=('glibc')
makedepends=('cmake')
source=("https://sourceforge.net/projects/matroska/files/mkvalidator/mkvalidator-${pkgver}.tar.bz2")
sha256sums=('f9eaa2138fade7103e6df999425291d2947c5355294239874041471e3aa243f0')

build() {
  cmake -S "mkvalidator-${pkgver}" -B build \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_POLICY_VERSION_MINIMUM=3.5

  cmake --build build
}

package() {
  install -Dm755 build/mkvalidator/mkvalidator "${pkgdir}/usr/bin/mkvalidator"
  install -Dm644 "mkvalidator-${pkgver}/ReadMe.txt" "${pkgdir}/usr/share/licenses/${pkgname}/License.txt"
}
