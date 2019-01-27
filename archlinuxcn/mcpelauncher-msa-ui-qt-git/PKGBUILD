# Maintainer: Paul <paul@mrarm.io>
pkgname=mcpelauncher-msa-ui-qt-git
pkgver=v0.1.beta.1.r10.g323bb82
pkgrel=1
pkgdesc="Microsoft Account authentication user interface (Qt) for the mcpelauncher-msa-daemon"
arch=('x86_64' 'i686')
url="https://github.com/minecraft-linux/msa-manifest"
license=('MIT' 'GPL3')
makedepends=('git' 'cmake')
depends=('qt5-base' 'qt5-webengine')
provides=('mcpelauncher-msa-ui' 'mcpelauncher-msa-ui-qt')
conflicts=('mcpelauncher-msa-ui-qt')
source=(
  'git://github.com/minecraft-linux/msa-manifest.git'
  'git://github.com/minecraft-linux/logger.git'
  'git://github.com/minecraft-linux/base64.git'
  'git://github.com/minecraft-linux/file-util.git'
  'git://github.com/minecraft-linux/arg-parser.git'
  'git://github.com/minecraft-linux/rapidxml.git'
  'git://github.com/MCMrARM/simple-ipc.git'
  'git://github.com/minecraft-linux/daemon-utils.git'
  'git://github.com/minecraft-linux/msa-daemon-client.git'
  'git://github.com/minecraft-linux/msa-ui-qt.git'
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
  git config submodule.msa-daemon-client.url $srcdir/msa-daemon-client
  git config submodule.msa-ui-qt.url $srcdir/msa-ui-qt
  git submodule update logger base64 file-util arg-parser rapidxml simple-ipc daemon-utils msa-daemon-client msa-ui-qt
}
build() {
  cd msa-manifest
  mkdir -p build
  cd build
  cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=RelWithDebInfo -DENABLE_MSA_DAEMON=OFF -DENABLE_MSA_QT_UI=ON ..
  make
}
package() {
  cd msa-manifest/build
  make DESTDIR="$pkgdir" install

  install -Dm644 ../msa-ui-qt/LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  install -Dm644 ../msa-daemon-client/LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE.MIT"
  install -Dm644 ../../nlohmann_json_license.txt "$pkgdir/usr/share/licenses/$pkgname/nlohmann_json_license.txt"
}
