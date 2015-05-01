# Maintainer: Antonio Rojas <arojas@archlinux.org>
# Contributor: Kuba Serafinowski <zizzfizzix(at)gmail(dot)com>

pkgname=kdeconnect-git
pkgver=r804.e34a291
pkgrel=1
pkgdesc='Adds communication between KDE and your smartphone'
arch=(i686 x86_64)
url='https://projects.kde.org/projects/playground/base/kdeconnect-kde'
license=(GPL2)
depends=(kio kcmutils qca-qt5 libfakekey hicolor-icon-theme)
makedepends=(extra-cmake-modules git python)
provides=(kdeconnect)
conflicts=(kdeconnect-frameworks kdeconnect)
replaces=(kdeconnect-frameworks-git)
source=("git://anongit.kde.org/kdeconnect-kde.git")
install=$pkgname.install
sha256sums=('SKIP')

pkgver() {
  cd kdeconnect-kde
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
  mkdir -p build
}

build() {
  cd build
  cmake ../kdeconnect-kde \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=Release \
    -DLIB_INSTALL_DIR=lib \
    -DLIBEXEC_INSTALL_DIR=lib \
    -DKDE_INSTALL_USE_QT_SYS_PATHS=ON
  make
}

package() {
  cd build
  make DESTDIR="$pkgdir" install
}
