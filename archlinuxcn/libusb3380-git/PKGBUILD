# Maintainer:  dreieck (https://aur.archlinux.org/account/dreieck)
# Contributor: Alexander Couzens <lynxis@fe80.eu> (https://aur.archlinux.org/account/lynxis)

pkgname=libusb3380-git
pkgver=r16.92d102a6b137
pkgrel=1
pkgdesc="USB3380 abstraction layer for libusb"
_gitname=libusb3380
arch=('armv7h' 'i686' 'x86_64')
url="https://github.com/xtrx-sdr/libusb3380"
license=('Apache-2.0')
makedepends=('git' 'cmake')
depends=(
  'glibc'
  'libusb'
  'libusb-compat'
)
source=("git+$url")
md5sums=('SKIP')
provides=('libusb3380')
conflicts=('libusb3380')

pkgver() {
  cd "$srcdir"/$_gitname
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short=12 HEAD)"
}

build() {
  mkdir -p "$srcdir"/$_gitname/build
  cd "$srcdir"/$_gitname/build

  cmake .. \
    -DBUILD_SHARED_LIBS=ON \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_POLICY_VERSION_MINIMUM=3.5

  make
}

package() {
  cd "$srcdir"/$_gitname/build

  make DESTDIR="$pkgdir" install
}

