# Maintainer:  Marcin (CTRL) Wieczorek <marcin@marcin.co>
# Contributor: Fredrik Haikarainen <fredrik.haikarainen@gmail.com>

pkgname=light
pkgver=1.0
pkgrel=2
pkgdesc='Program to easily change brightness on backlight-controllers.'
arch=('i686' 'x86_64')
url="https://github.com/haikarainen/light"
license=('GPL3')
makedepends=('help2man')
source=("https://github.com/haikarainen/light/archive/v${pkgver}.tar.gz")
sha256sums=('974608ee42ffe85cfd23184306d56d86ec4e6f4b0518bafcb7b3330998b1af64')

build() {
  cd "${srcdir}/light-${pkgver}"
  make
}

package() {
  cd "${srcdir}/light-${pkgver}"
  make DESTDIR="${pkgdir}/" install
}
