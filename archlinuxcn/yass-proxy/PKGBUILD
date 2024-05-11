# Maintainer: Chilledheart <hukeyue@hotmail.com>
# Contributor: Chilledheart <hukeyue@hotmail.com>

pkgname=yass-proxy
pkgver=1.9.5
pkgrel=3
_pkgver=1.9.5
_pkgrel=1
pkgdesc="lightweight http/socks proxy"
arch=(x86_64)
url="https://github.com/Chilledheart/yass"
license=(GPL-2.0-only)
depends=(gcc-libs glibc gtk4 zlib libnghttp2 c-ares)
optdepends=(gtk-update-icon-cache)
makedepends=(git ninja perl pkg-config cmake gtk4 gettext curl go clang lld llvm)
checkdepends=(curl)
provides=(yass-proxy)
conflicts=(yass-proxy-git)
source=("https://github.com/Chilledheart/yass/releases/download/${_pkgver}/yass-${_pkgver}.tar.bz2"
        "boringssl-gcc-14.patch"
        "libcxx-gcc-14.patch"
        "cmake.patch"
        )
sha256sums=('26e013c811f0b4cb194bfd4587fa6e644b5f155593df0c6a15c026120084a635'
            '6201584f8c5c983405e07f99a83e33a28e1aa907a752bc07bc641d0cf1087662'
            '72f55c55adb141d31dd9cd892cd04a08df2d95a1d94ad3a4b421a312075782e4'
            '24cef2470a32381e771ce110e5bae4f1f96e589e9d59a3aa6c294ba5cf6a8d71'
            )

prepare() {
  SRC_DIR="${srcdir}/yass-${_pkgver}"
  pushd $SRC_DIR
  patch --forward --strip=1 --input=../boringssl-gcc-14.patch
  patch --forward --strip=1 --input=../libcxx-gcc-14.patch
  patch --forward --strip=1 --input=../cmake.patch
  cd tools
  go build
  cd ..
  popd
}

build(){
  SRC_DIR="${srcdir}/yass-${_pkgver}"
  pushd $SRC_DIR
  export CC=clang
  export CXX=clang++
  rm -rf build-linux-amd64
  mkdir build-linux-amd64
  cd build-linux-amd64
  cmake .. -DGUI=ON -DCMAKE_BUILD_TYPE=Release -G Ninja -DBUILD_TESTS=on \
    -DUSE_SYSTEM_ZLIB=on -DUSE_SYSTEM_CARES=on -DUSE_SYSTEM_NGHTTP2=on \
    -DCMAKE_INSTALL_PREFIX=/usr -DCLI=off -DSERVER=off \
    -DUSE_LIBCXX=on -DENABLE_LTO=on -DUSE_TCMALLOC=on
  ninja yass yass_test
  llvm-objcopy --strip-debug yass
  cd ..

  popd
}

check() {
  SRC_DIR="${srcdir}/yass-${_pkgver}"
  pushd $SRC_DIR
  ./build-linux-amd64/yass_test
  popd
}

package(){
  SRC_DIR="${srcdir}/yass-${_pkgver}"
  pushd $SRC_DIR

  install -Dm644 ./build-linux-amd64/LICENSE ${pkgdir}/usr/share/licenses/yass/LICENSE
  DESTDIR=${pkgdir} ninja -C build-linux-amd64 install
  rm -rf ${pkgdir}/usr/share/doc

  popd
}
