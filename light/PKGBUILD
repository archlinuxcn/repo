# Maintainer:  Marcin (CTRL) Wieczorek <marcin@marcin.co>
# Contributor: Fredrik Haikarainen <fredrik.haikarainen@gmail.com>

pkgname=light
pkgver=1.1.2
pkgrel=1
pkgdesc='Program to easily change brightness on backlight-controllers.'
arch=('i686' 'x86_64')
url="https://github.com/haikarainen/light"
license=('GPL3')
makedepends=('help2man')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/haikarainen/light/archive/${pkgver}.tar.gz")
sha256sums=('291ef234929adb20fe96359724c5ccad36cf396dd110f7001654c21e17800032')

build() {
  cd "${srcdir}/light-${pkgver}"
  make
}

package() {
  cd "${srcdir}/light-${pkgver}"
  make DESTDIR="${pkgdir}/" install
}
