# Maintainer:  Marcin (CTRL) Wieczorek <marcin@marcin.co>
# Contributor: Fredrik Haikarainen <fredrik.haikarainen@gmail.com>

pkgname=light
pkgver=1.2
pkgrel=1
pkgdesc='Program to easily change brightness on backlight-controllers.'
arch=('i686' 'x86_64')
url="https://github.com/haikarainen/light"
license=('GPL3')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/haikarainen/light/archive/v${pkgver}.tar.gz")
sha256sums=('27dd588f06afbaabf6050abdf5bddc571c71ff26451e3ac6d1f116f80ed7dbbd')

build() {
  cd "${srcdir}/light-${pkgver}"
  ./autogen.sh
  ./configure --prefix=/usr
  make
}

package() {
  cd "${srcdir}/light-${pkgver}"
  make DESTDIR="${pkgdir}/" PREFIX=/usr install
}
