# Maintainer: xsmile <>

pkgname=uefitool-git
_pkgname=uefitool
_tools=(UEFIPatch UEFIReplace)
pkgver=r228.44cafeb
pkgrel=1
pkgdesc='UEFI firmware image viewer and editor and utilities'
arch=(any)
url=https://github.com/LongSoft/UEFITool
license=(BSD)
depends=(qt5-base)
makedepends=(git)
provides=($_pkgname)
conflicts=($_pkgname)
source=("${_pkgname}::git+${url}.git")
md5sums=('SKIP')

pkgver() {
  cd "$srcdir/$_pkgname"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

_build() {
  qmake \
    QMAKE_CFLAGS_RELEASE="$CFLAGS" \
    QMAKE_CXXFLAGS_RELEASE="$CXXFLAGS" \
    QMAKE_LFLAGS_RELEASE="$LDFLAGS"
  make
}

build() {
  # UEFITool
  cd "$srcdir/$_pkgname"
  _build
  # Other tools
  for tool in "${_tools[@]}"; do
    cd "$srcdir/$_pkgname/$tool"
    _build
  done
}

package() {
  # UEFITool
  cd "$srcdir/$_pkgname"
  install -Dm755 UEFITool "$pkgdir/usr/bin/$_pkgname"
  # Other tools
  for tool in "${_tools[@]}"; do
    install -Dm755 "$tool/$tool" "$pkgdir/usr/bin/${tool,,}"
  done
  # Patch files
  install -Dm644 UEFIPatch/patches{,-misc}.txt -t "$pkgdir/usr/share/$_pkgname/"
  # License
  install -Dm644 LICENSE.md -t "$pkgdir/usr/share/licenses/$_pkgname/"
}
