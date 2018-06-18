# Maintainer:  Marcin (CTRL) Wieczorek <marcin@marcin.co>
# Contributor: Fredrik Haikarainen <fredrik.haikarainen@gmail.com>

pkgname=light
pkgver=1.1
pkgrel=1
pkgdesc='Program to easily change brightness on backlight-controllers.'
arch=('i686' 'x86_64')
url="https://github.com/haikarainen/light"
license=('GPL3')
makedepends=('help2man')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/haikarainen/light/archive/${pkgver}.tar.gz")
sha256sums=('1f80b1fe3244d1c656677a92db0747a5af86dab93c1afe7b78c2732ab0c431b2')

build() {
  cd "${srcdir}/light-${pkgver}"
  make
}

package() {
  cd "${srcdir}/light-${pkgver}"
  make DESTDIR="${pkgdir}/" install
}
