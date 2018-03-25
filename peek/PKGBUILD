# Maintainer: Philipp Wolfer <ph.wolfer@gmail.com>
pkgname=peek
pkgver=1.3.0
pkgrel=1
pkgdesc="Simple screen recorder with an easy to use interface"
arch=('i686' 'x86_64')
url="https://github.com/phw/peek"
license=('GPL3')
depends=(gtk3 libkeybinder3 ffmpeg)
makedepends=(cmake vala gettext txt2man)
optdepends=(
  'gst-plugins-good: Recording under Gnome Shell'
  'gst-plugins-ugly: MP4 output under Gnome Shell'
  'gifski: High quality GIF animations with thousands of colors'
)
source=(${pkgname}-${pkgver}.tar.gz::https://github.com/phw/${pkgname}/archive/${pkgver}.tar.gz)
sha256sums=('0d20741663e9a173151d8371df3cb90f8f542033640ce99a4863803cd0f32cb4')

prepare() {
  mkdir -p build
}

build() {
  cd "build"
  cmake "${srcdir}/${pkgname}-${pkgver}" \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DBUILD_TESTS=ON \
    -DCMAKE_BUILD_TYPE=Release \
    -DGSETTINGS_COMPILE=OFF \
    -DENABLE_FILECHOOSERNATIVE=ON
  make
}

check() {
  cd "build"
  make test
}

package() {
  cd "build"
  make DESTDIR=${pkgdir} install
}
