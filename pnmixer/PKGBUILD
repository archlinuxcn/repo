# Maintainer: Brian Bidulock <bidulock@openss7.org>
pkgname=pnmixer
pkgver=0.7.2
pkgrel=1
pkgdesc="GTK volume mixer applet that runs in the system tray."
arch=('i686' 'x86_64')
license=('GPL')
url="https://github.com/nicklan/pnmixer"
makedepends=('intltool' 'cmake')
depends=('gtk2' 'alsa-lib' 'libnotify')
source=("https://github.com/nicklan/pnmixer/releases/download/v${pkgver}/pnmixer-v${pkgver}.tar.gz")
md5sums=('e9f17f56c50de39393030a96e343427b')
build() {
  cd $pkgname-v$pkgver
  cmake \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_SKIP_RPATH=ON \
    -DWITH_GTK3=OFF
  make
}
package() {
  cd $pkgname-v$pkgver
  make DESTDIR="$pkgdir" install
}
