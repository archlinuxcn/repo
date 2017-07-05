# Maintainer: Shengyu Zhang <arch#srain.im>
pkgname=pnmixer-gtk3
pkgver=0.7.2
pkgrel=2
pkgdesc="A simple mixer application designed to run in your system tray."
arch=('i686' 'x86_64')
license=('GPL')
url="https://github.com/nicklan/pnmixer"
depends=('gtk3' 'alsa-lib' 'libx11' 'libnotify')
makedepends=('cmake' 'pkg-config' 'gettext')
conflicts=('pnmixer-git' 'pnmixer-gtk2' 'pnmixer')

source=(https://github.com/nicklan/pnmixer/archive/v${pkgver}.tar.gz)
sha256sums=('433487da386396f8d39244395220992ff73fe5191d0226febaead403a0cd6f2c')

build() {
  cd ${pkgname%-gtk3}-$pkgver

  cmake \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_SKIP_RPATH=ON \
    -DWITH_GTK3=ON
  make
}

package() {
  cd ${pkgname%-gtk3}-$pkgver

  make DESTDIR="$pkgdir" install
}
