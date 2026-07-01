# Maintainer: blacktav <blacktav at gmail dot com>
# Maintainer: Lufalas <lufalas at posteo dot com>
# Contributor: based on unknown abandoned pokerth-final from 2012-12-27
# Patches: xx55tt, viktoracoric, Mailaender, jlocash

pkgname=pokerth
pkgver=2.0.8
pkgrel=2

pkgdesc="Client to online Poker game written in C++/Qt"
arch=('x86_64')
url="http://www.pokerth.net/"
license=('AGPL-3.0-only' 'LicenseRef-custom')
depends=(
   'qt6-base'
   'qt6-declarative'
   'qt6-multimedia'
   'boost-libs'
   'protobuf'
)

makedepends=(
   'boost'
   'cmake'
   'ninja'
   'qt6-svg'
   'qt6-tools'
   'qt6-websockets'
)

source=("${pkgname}-${pkgver}.tar.gz::https://github.com/pokerth/pokerth/archive/refs/tags/v${pkgver}.tar.gz")
md5sums=('fff1ad64ae638c387c2acf144390ad94')

build() {
  local cmake_options=(
    -B build
    -S ${pkgname}-${pkgver}
    -G Ninja
    -DCMAKE_INSTALL_PREFIX=/usr
    -DCMAKE_BUILD_TYPE:STRING=None
    -DCMAKE_C_FLAGS="${CFLAGS} -DNDEBUG"
    -DCMAKE_CXX_FLAGS="${CXXFLAGS} -DNDEBUG"
    -Wno-dev
  )
  cmake "${cmake_options[@]}"
  cmake --build build --target all --
}

package() {
  DESTDIR="${pkgdir}" cmake --install build

  cd "${pkgname}-${pkgver}"

  install -Dm644 docs/pokerth.1 "${pkgdir}/usr/share/man/man1/pokerth.1"
  mkdir -p "${pkgdir}/usr/share/doc/${pkgname}"
  install -Dm644 docs/gui_styling_howto.txt "${pkgdir}/usr/share/doc/pokerth/"
  install -Dm644 docs/server_setup_howto.txt "${pkgdir}/usr/share/doc/pokerth/"
  install -Dm644 data/data-copyright.txt "${pkgdir}/usr/share/licenses/pokerth/LICENSE"
  install -Dm644 pokerth.svg "${pkgdir}/usr/share/icons/hicolor/scalable/apps/pokerth.svg"

  rm "${pkgdir}/usr/share/pokerth/data/data-copyright.txt"
}

