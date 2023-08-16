# Maintainer: noodlefighter <noodlefighter#gmail.com>
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: GONG Chen <chen dot sst at gmail dot com>
# Contributor: 網軍總司令

_pkgname=librime
pkgname=$_pkgname-sbxlm
pkgver=9.5.14
_octagramcommit=f92e083052b9983ee3cbddcda5ed60bb3c068e24
_luacommit=d45a41af2f9d731e3c1516a191cc3160e3cb8377
pkgrel=1
epoch=1
pkgdesc="Rime input method engine (声笔系列码)"
arch=('x86_64')
url="https://github.com/sbxlmdsl/librime"
license=('GPL3')
depends=('boost-libs' 'capnproto' 'opencc' 'yaml-cpp' 'leveldb' 'librime-data' 'lua' 'google-glog' 'marisa')
makedepends=('cmake' 'boost' 'gtest' 'ninja')
provides=("$_pkgname")
conflicts=("$_pkgname")
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/${pkgver}.tar.gz"
        "https://github.com/lotem/librime-octagram/archive/$_octagramcommit/librime-octagram-$_octagramcommit.tar.gz"
        "https://github.com/hchunhui/librime-lua/archive/$_luacommit/librime-lua-$_luacommit.tar.gz")
sha512sums=('76d95c8b41faf53aa7253469dc628561bf93cdc8d3cfd790ce6d984375983f6eb66e695bea3887a97d20c19221711551526d065fa317f64abee42f1188545864'
            '737d1c58982d2f79a6e8b2548eefa1dddc036dd6e6d5436e7d6b4f3adfa2e9d8e45b29a13c1b8207a93cb77f3b5dbd9d18436f44d4e8040eb95b962de582b386'
            '2a3d3b49d53066fe96dd008e8064718082225e6bf185574a25b8e98175d9936abcfa1fdc56e48f9c72a2deb46f8157d6132fd119ff8e0a3d52fbe9e2ea21386c')

prepare() {
  cd "$srcdir/${_pkgname}-${pkgver}"
  cd plugins
  ln -sf "$srcdir"/librime-octagram-$_octagramcommit librime-octagram
  ln -sf "$srcdir"/librime-lua-$_luacommit librime-lua
}

build() {
  cd "${_pkgname}-${pkgver}"
  export CXXFLAGS="$CXXFLAGS -DNDEBUG"
  cmake . -GNinja -Bbuild -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_MERGED_PLUGINS=Off -DENABLE_EXTERNAL_PLUGINS=On
  cmake --build build
}

check() {
  cd "${_pkgname}-${pkgver}/build"
  ninja test
}

package() {
  cd "${_pkgname}-${pkgver}/build"
  DESTDIR="$pkgdir" ninja install
}
