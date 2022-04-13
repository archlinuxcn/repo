# Maintainer: Chih-Hsuan Yen <base64_decode("eWFuMTIxMjUgQVQgYXJjaGxpbnV4IERPVCBvcmc=")>

_pkgname=qtxdg-tools
pkgname=$_pkgname-git
pkgver=0.0.0.r23.891ee9e
pkgrel=1
pkgdesc="libqtxdg user tools"
arch=("x86_64")
url="https://github.com/lxqt/qtxdg-tools"
license=("LGPL2.1")
depends=("qt5-base" "libqtxdg-git")
makedepends=("git" "cmake" "qt5-tools" "lxqt-build-tools-git")
provides=("$_pkgname=$pkgver")
conflicts=("$_pkgname")
source=("git+https://github.com/lxqt/$_pkgname.git")
sha256sums=('SKIP')

pkgver() {
  cd "$srcdir/$_pkgname"
  printf "0.0.0.r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
  cmake -B build -S "$srcdir/$_pkgname" \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=lib
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
}
