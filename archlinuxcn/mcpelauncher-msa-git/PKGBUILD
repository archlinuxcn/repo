# Maintainer: Paul <paul@mrarm.io>
pkgname=mcpelauncher-msa-git
pkgver=v0.1.beta.1.r10.g323bb82
pkgrel=1
pkgdesc="Microsoft Account authentication daemon for mcpelauncher"
arch=('x86_64' 'i686')
url="https://github.com/minecraft-linux/msa-manifest"
license=('MIT')
makedepends=('git' 'cmake')
depends=('curl' 'openssl')
provides=('mcpelauncher-msa')
conflicts=('mcpelauncher-msa')
source=(
  'git://github.com/minecraft-linux/msa-manifest.git'
  'git://github.com/minecraft-linux/logger.git'
  'git://github.com/minecraft-linux/base64.git'
  'git://github.com/minecraft-linux/file-util.git'
  'git://github.com/minecraft-linux/arg-parser.git'
  'git://github.com/minecraft-linux/rapidxml.git'
  'git://github.com/MCMrARM/simple-ipc.git'
  'git://github.com/minecraft-linux/daemon-utils.git'
  'git://github.com/minecraft-linux/msa.git'
  'git://github.com/minecraft-linux/msa-daemon.git'
  'git://github.com/minecraft-linux/msa-daemon-client.git'
  'nlohmann_json_license.txt::https://raw.githubusercontent.com/nlohmann/json/develop/LICENSE.MIT'
)
md5sums=(
  'SKIP'
  'SKIP'
  'SKIP'
  'SKIP'
  'SKIP'
  'SKIP'
  'SKIP'
  'SKIP'
  'SKIP'
  'SKIP'
  'SKIP'
  'SKIP'
)

pkgver() {
  cd "msa-manifest"
  git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}
prepare() {
  cd msa-manifest
  git submodule init
  git config submodule.logger.url $srcdir/logger
  git config submodule.base64.url $srcdir/base64
  git config submodule.file-util.url $srcdir/file-util
  git config submodule.arg-parser.url $srcdir/arg-parser
  git config submodule.rapidxml.url $srcdir/rapidxml
  git config submodule.simple-ipc.url $srcdir/simple-ipc
  git config submodule.daemon-utils.url $srcdir/daemon-utils
  git config submodule.msa.url $srcdir/msa
  git config submodule.msa-daemon.url $srcdir/msa-daemon
  git config submodule.msa-daemon-client.url $srcdir/msa-daemon-client
  git submodule update logger base64 file-util arg-parser rapidxml simple-ipc daemon-utils msa msa-daemon msa-daemon-client
}
build() {
  cd msa-manifest
  mkdir -p build
  cd build
  cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=RelWithDebInfo -DMSA_UI_PATH_DEV=OFF ..
  make
}
package() {
  cd msa-manifest/build
  make DESTDIR="$pkgdir" install

  install -Dm644 ../msa-daemon/LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  install -Dm644 ../../nlohmann_json_license.txt "$pkgdir/usr/share/licenses/$pkgname/nlohmann_json_license.txt"
  install -Dm644 ../rapidxml/license.txt "$pkgdir/usr/share/licenses/$pkgname/rapidxml_license.txt"
}
