# Maintainer: Paul <paul@mrarm.io>
pkgname=mcpelauncher-linux-git
pkgver=v0.1.beta.2.r11.gc2a2f53
pkgrel=1
pkgdesc="Minecraft: Pocket Edition launcher for Linux"
arch=('x86_64' 'i686')
url="https://github.com/minecraft-linux/mcpelauncher-manifest"
license=('GPL3' 'custom')
makedepends_x86_64=('git' 'cmake' 'gcc-multilib')
makedepends_i686=('git' 'cmake' 'gcc')
depends_x86_64=('lib32-curl' 'lib32-libx11' 'lib32-zlib' 'lib32-libpng' 'lib32-libevdev' 'lib32-systemd' 'lib32-libxi' 'lib32-libegl')
depends_i686=('curl' 'libx11' 'zlib' 'libpng' 'libevdev' 'systemd' 'libxi' 'libegl')
optdepends=('mcpelauncher-msa: Xbox Live support')
provides=('mcpelauncher-client' 'mcpelauncher-server')
conflicts=('mcpelauncher-client' 'mcpelauncher-server')
source=(
  'git://github.com/minecraft-linux/mcpelauncher-manifest.git'
  'git://github.com/minecraft-linux/logger.git'
  'git://github.com/minecraft-linux/base64.git'
  'git://github.com/minecraft-linux/file-util.git'
  'git://github.com/minecraft-linux/properties-parser.git'
  'git://github.com/minecraft-linux/arg-parser.git'
  'git://github.com/MCMrARM/simple-ipc.git'
  'git://github.com/minecraft-linux/daemon-utils.git'
  'git://github.com/minecraft-linux/msa-daemon-client.git'
  'git://github.com/minecraft-linux/libhybris.git'
  'git://github.com/minecraft-linux/eglut.git'
  'git://github.com/MCMrARM/linux-gamepad.git'
  'git://github.com/minecraft-linux/game-window.git'
  'git://github.com/minecraft-linux/file-picker.git'
  'git://github.com/minecraft-linux/cll-telemetry.git'
  'git://github.com/minecraft-linux/minecraft-symbols.git'
  'git://github.com/minecraft-linux/minecraft-imported-symbols.git'
  'git://github.com/minecraft-linux/mcpelauncher-common.git'
  'git://github.com/minecraft-linux/mcpelauncher-core.git'
  'git://github.com/minecraft-linux/mcpelauncher-client.git'
  'git://github.com/minecraft-linux/mcpelauncher-server.git'
  'git://github.com/minecraft-linux/mcpelauncher-just.git'
  'git://github.com/minecraft-linux/mcpelauncher-linux-bin.git'
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
  cd mcpelauncher-manifest
  git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}
prepare() {
  cd mcpelauncher-manifest
  git submodule init
  git config submodule.logger.url $srcdir/logger
  git config submodule.base64.url $srcdir/base64
  git config submodule.file-util.url $srcdir/file-util
  git config submodule.properties-parser.url $srcdir/properties-parser
  git config submodule.simple-ipc.url $srcdir/simple-ipc
  git config submodule.daemon-utils.url $srcdir/daemon-utils
  git config submodule.msa-daemon-client.url $srcdir/msa-daemon-client
  git config submodule.libhybris.url $srcdir/libhybris
  git config submodule.eglut.url $srcdir/eglut
  git config submodule.linux-gamepad.url $srcdir/linux-gamepad
  git config submodule.game-window.url $srcdir/game-window
  git config submodule.file-picker.url $srcdir/file-picker
  git config submodule.cll-telemetry.url $srcdir/cll-telemetry
  git config submodule.minecraft-symbols.url $srcdir/minecraft-symbols
  git config submodule.minecraft-imported-symbols.url $srcdir/minecraft-imported-symbols
  git config submodule.mcpelauncher-common.url $srcdir/mcpelauncher-common
  git config submodule.mcpelauncher-core.url $srcdir/mcpelauncher-core
  git config submodule.mcpelauncher-client.url $srcdir/mcpelauncher-client
  git config submodule.mcpelauncher-server.url $srcdir/mcpelauncher-server
  git config submodule.mcpelauncher-just.url $srcdir/mcpelauncher-just
  git config submodule.arg-parser.url $srcdir/arg-parser
  git config submodule.mcpelauncher-linux-bin.url $srcdir/mcpelauncher-linux-bin
  git submodule update logger base64 file-util properties-parser simple-ipc daemon-utils msa-daemon-client libhybris eglut linux-gamepad game-window file-picker cll-telemetry minecraft-symbols minecraft-imported-symbols mcpelauncher-common mcpelauncher-core mcpelauncher-client mcpelauncher-server mcpelauncher-just arg-parser mcpelauncher-linux-bin
}
build() {
  cd mcpelauncher-manifest
  mkdir -p build
  cd build
  cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=RelWithDebInfo -DENABLE_DEV_PATHS=OFF ..
  make
}
package() {
  cd mcpelauncher-manifest/build
  make DESTDIR="$pkgdir" install

  install -Dm644 ../LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  install -Dm644 ../msa-daemon-client/LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE.MIT"
  install -Dm644 ../mcpelauncher-linux-bin/FMod\ License.txt "$pkgdir/usr/share/licenses/$pkgname/fmod_license.txt"
  install -Dm644 ../libhybris/LICENSE "$pkgdir/usr/share/licenses/$pkgname/libhybris_license.txt"
  install -Dm644 ../eglut/LICENSE "$pkgdir/usr/share/licenses/$pkgname/eglut_license.txt"
  install -Dm644 ../../nlohmann_json_license.txt "$pkgdir/usr/share/licenses/$pkgname/nlohmann_json_license.txt"
}
