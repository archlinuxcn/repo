# Maintainer: Paul <paul@mrarm.io>
pkgname=mcpelauncher-ui-git
pkgver=v0.1.beta.1.r1.gb3f9c5a
pkgrel=1
pkgdesc="Minecraft: PE Linux launcher UI"
arch=('x86_64' 'i686')
url="https://github.com/minecraft-linux/mcpelauncher-ui-manifest"
license=('GPL3', 'MIT')
makedepends=('git' 'cmake')
depends=('qt5-base' 'qt5-webengine' 'qt5-declarative' 'qt5-quickcontrols' 'qt5-quickcontrols2' 'qt5-svg' 'libzip' 'protobuf' 'mcpelauncher-client')
provides=('mcpelauncher-ui')
conflicts=('mcpelauncher-ui')
source=(
  'git://github.com/minecraft-linux/mcpelauncher-ui-manifest.git'
  'git://github.com/minecraft-linux/file-util.git'
  'git://github.com/MCMrARM/axml-parser.git'
  'git://github.com/minecraft-linux/mcpelauncher-apkinfo.git'
  'git://github.com/minecraft-linux/mcpelauncher-extract.git'
  'google-play-api::git://github.com/MCMrARM/Google-Play-API.git'
  'git://github.com/minecraft-linux/playdl-signin-ui-qt.git'
  'git://github.com/minecraft-linux/mcpelauncher-ui-qt.git'
  'git://github.com/minecraft-linux/mcpelauncher-proprietary.git'
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
)

pkgver() {
  cd "mcpelauncher-ui-manifest"
  git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}
prepare() {
  cd mcpelauncher-ui-manifest
  git submodule init
  git config submodule.file-util.url $srcdir/file-util
  git config submodule.axml-parser.url $srcdir/axml-parser
  git config submodule.mcpelauncher-apkinfo.url $srcdir/mcpelauncher-apkinfo
  git config submodule.mcpelauncher-extract.url $srcdir/mcpelauncher-extract
  git config submodule.google-play-api.url $srcdir/google-play-api
  git config submodule.playdl-signin-ui-qt.url $srcdir/playdl-signin-ui-qt
  git config submodule.mcpelauncher-ui-qt.url $srcdir/mcpelauncher-ui-qt
  git submodule update file-util axml-parser mcpelauncher-apkinfo mcpelauncher-extract google-play-api playdl-signin-ui-qt mcpelauncher-ui-qt
  cd mcpelauncher-ui-qt
  git submodule init
  git config submodule.Resources/proprietary.url $srcdir/mcpelauncher-proprietary
  git submodule update Resources/proprietary
}
build() {
  cd mcpelauncher-ui-manifest
  mkdir -p build
  cd build
  cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=RelWithDebInfo ..
  make
}
package() {
  cd mcpelauncher-ui-manifest/build
  make DESTDIR="$pkgdir" install
  install -Dm644 ../mcpelauncher-ui-qt/LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  install -Dm644 ../../nlohmann_json_license.txt "$pkgdir/usr/share/licenses/$pkgname/nlohmann_json_license.txt"
}
