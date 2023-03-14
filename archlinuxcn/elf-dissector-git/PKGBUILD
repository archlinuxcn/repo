# Maintainer: João Figueiredo & chaotic-aur <islandc0der@chaotic.cx>

pkgname=elf-dissector-git
pkgver=0.0.1_r783.g368d2a0
pkgrel=1
pkgdesc='Static analysis tool for ELF libraries and executables'
arch=($CARCH)
url='https://invent.kde.org/sdk/elf-dissector'
license=(GPL)
depends=(harfbuzz hicolor-icon-theme libdwarf qt5-base)
makedepends=(extra-cmake-modules-git git kitemmodels-git)
optdepends=('capstone: disassembler' 'gnuplot: performance plot')
source=("git+https://github.com/KDE/${pkgname%-git}.git")
sha256sums=('SKIP')

pkgver() {
  cd ${pkgname%-git}
  _ver="$(grep -m1 'project(elf-dissector VERSION' CMakeLists.txt | cut -d ' ' -f3 | tr - . | tr -d ')')"
  echo "${_ver}_r$(git rev-list --count HEAD).g$(git rev-parse --short HEAD)"
}

build() {
  cmake -B build -S ${pkgname%-git} \
    -DBUILD_TESTING=OFF
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
}
