# Maintainer: Keeyou <keeyou-cn@outlook.com>
# Contributor: Keeyou <keeyou-cn@outlook.com>

pkgname=yass-proxy
pkgver=1.16.0
pkgrel=1
_pkgver=1.16.0
_pkgrel=1
pkgdesc="lightweight http/socks proxy"
arch=(x86_64)
url="https://github.com/Chilledheart/yass"
license=(GPL-2.0-only)
depends=(gcc-libs glibc gtk4 zlib libnghttp2 c-ares gperftools jsoncpp)
optdepends=(gtk-update-icon-cache)
makedepends=(gcc binutils git ninja perl pkg-config cmake gettext curl go)
checkdepends=(curl)
provides=(yass-proxy)
conflicts=(yass-proxy-git)
source=("https://github.com/Chilledheart/yass/releases/download/${_pkgver}/yass-${_pkgver}.tar.zst"
        )
sha256sums=('fdb6b801c0852aaae17a20d0cbda5b565be38605c0bc56a1d8c614633da8ecdd')

build(){
  SRC_DIR="${srcdir}/yass-${_pkgver}"
  pushd $SRC_DIR
  rm -rf build
  mkdir build
  cd build
  cmake .. -DCMAKE_BUILD_TYPE=Release -G Ninja -DBUILD_TESTS=on \
    -DUSE_TCMALLOC=on -DUSE_SYSTEM_TCMALLOC=on \
    -DUSE_ZLIB=on -DUSE_CARES=on \
    -DUSE_SYSTEM_ZLIB=on -DUSE_SYSTEM_CARES=on -DUSE_SYSTEM_NGHTTP2=on \
    -DUSE_JSONCPP=on -DUSE_SYSTEM_JSONCPP=on \
    -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_SYSCONFDIR=/etc \
    -DUSE_CET=on \
    -DGUI=ON -DUSE_GTK4=on -DCLI=off -DSERVER=off
  ninja yass yass_test
  cd ..

  popd
}

check() {
  SRC_DIR="${srcdir}/yass-${_pkgver}"
  pushd $SRC_DIR
  ./build/yass_test
  popd
}

package(){
  SRC_DIR="${srcdir}/yass-${_pkgver}"
  pushd $SRC_DIR

  install -Dm644 ./build/LICENSE ${pkgdir}/usr/share/licenses/yass/LICENSE
  DESTDIR=${pkgdir} ninja -C build install
  rm -rf ${pkgdir}/usr/share/doc

  popd
}
