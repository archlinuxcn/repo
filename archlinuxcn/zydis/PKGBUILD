# Maintainer: Thibaut Pérami <thibaut.perami@cl.cam.ac.uk>

pkgname=zydis
pkgver=4.0.0
pkgrel=1
pkgdesc="The ultimate, open-source X86 & X86-64 decoder/disassembler library."
arch=('x86_64')
url="https://zydis.re"
license=('MIT')
depends=('gcc-libs' 'zycore-c')
provides=('libZydis.so')
makedepends=('cmake')
source=("https://github.com/zyantific/zydis/archive/v${pkgver}.tar.gz")
sha256sums=('14e991fd97b021e15c77a4726a0ae8a4196d6521ab505acb5c51fc2f9be9530a')

prepare() {
  cd "${pkgname}-${pkgver}"
}

build() {
  cd "${pkgname}-${pkgver}"
  cmake -B build -Wno-dev\
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DZYDIS_BUILD_SHARED_LIB=ON \
        -DZYAN_SYSTEM_ZYCORE=true
  cmake --build build
}

package() {
  cd "${pkgname}-${pkgver}"
  DESTDIR="${pkgdir}" cmake --install build
  install -Dm644 -t "$pkgdir"/usr/share/licenses/$pkgname LICENSE
}
