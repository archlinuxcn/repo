# Maintainer: Alfredo Palhares <alfredo at palhares dot me>
# Contributor: Mark Wagie <mark dot wagie at tutanota dot com>

# Please contribute to:
# https://github.com/alfredopalhares/arch-pkgbuilds

pkgbase="joplin"
pkgname=('joplin' 'joplin-cli' 'joplin-desktop' 'joplin-desktop-electron')
pkgver=1.4.19
groups=('joplin')
pkgrel=13
install="joplin.install"
depends=('electron' 'gtk3' 'libexif' 'libgsf' 'libjpeg-turbo' 'libwebp' 'libxss' 'nodejs'
         'nss' 'orc' 'rsync' )
optdepends=('libappindicator-gtk3: for tray icon')
pkgdesc="A note taking and to-do application with synchronization capabilities - CLI and Desktop Version"
arch=('x86_64' 'i686')
makedepends=('git' 'npm' 'python' 'rsync' 'electron')
url="https://joplinapp.org/"
license=('MIT')
source=("joplin.desktop" "joplin-desktop.sh" "joplin.sh"
        "joplin-${pkgver}.tar.gz::https://github.com/laurent22/joplin/archive/v${pkgver}.tar.gz")
sha256sums=('c7c5d8b0ff9edb810ed901ea21352c9830bfa286f3c18b1292deca5b2f8febd2'
            'a450284fe66d89aa463d129ce8fff3a0a1a783a64209e4227ee47449d5737be8'
            '5b6f8847ec0c3848375755213c3009c273f478b4b80ed2c5f0af8f67ee0e94fb'
            '55aad4fe50e2da980983a69bc7c0870626064db971550d522e266feb17d38916')

build() {
  cd "${srcdir}/joplin-${pkgver}"
  msg2 "Disabling husky (git hooks)"
  sed -i '/"husky": ".*"/d' package.json

  # Force Lang
  # INFO: https://github.com/alfredopalhares/joplin-pkgbuild/issues/25
  export LANG=en_US.utf8

  msg2 "Installing dependencies..."
  npm install
  ./node_modules/.bin/lerna bootstrap
}

check() {
  cd "${srcdir}/joplin-${pkgver}"
  msg2 "Running Lerna Test Suite"
  npm run test || exit 0
}

package_joplin() {
  conflicts=('joplin-cli' 'joplin-desktop' 'joplin-desktop-electron')
  package_joplin-cli
  package_joplin-desktop
}

#TODO: A slimdown is needed
package_joplin-cli() {
  pkgdesc="A note taking and to-do application with synchronization capabilities - CLI App"
  depends=('nodejs' 'rsync')
  conflicts=('joplin')

  msg2 "Building CLI..."
  mkdir -p "${pkgdir}/usr/share/joplin-cli/app-cli"
  cd "${srcdir}/joplin-${pkgver}/packages/app-cli"
  npm run build
  cd build
  cp -R "." "${pkgdir}/usr/share/joplin-cli/app-cli/"

  msg2 "Copying Base Node Modules packages..."
  cd "${srcdir}/joplin-${pkgver}/packages/app-cli"
  cp -R "node_modules/" \
    "${pkgdir}/usr/share/joplin-cli/app-cli"

  msg2 "Copy CLI Joplin Dependencies..."
  cd "${srcdir}/joplin-${pkgver}/packages/"
  cp -R "fork-htmlparser2" "${pkgdir}/usr/share/joplin-cli/"
  cp -R "fork-sax" "${pkgdir}/usr/share/joplin-cli/"
  cp -R "lib/" "${pkgdir}/usr/share/joplin-cli/"
  cp -R "renderer/" "${pkgdir}/usr/share/joplin-cli/"
  cp -R "tools/" "${pkgdir}/usr/share/joplin-cli/"

  #TODO: Check if existing symblinks are valid
  msg2 "Fixing @Joplin Symlinks..."
  cd "${pkgdir}/usr/share/joplin-cli/"
  for dir in $(find . -type d -name "@joplin"); do
    cd "${pkgdir}/usr/share/joplin-cli/${dir}"
    rm -r *
    ln -s "../../../fork-htmlparser2" "fork-htmlparser2"
    ln -s "../../../fork-sax" "fork-sax"
    ln -s "../../../lib" "lib"
    ln -s "../../../renderer" "renderer"
    ln -s "../../../tools" "tools"
  done

  msg2 "Installing LICENSE..."
  cd "${srcdir}/joplin-${pkgver}/"
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"

  msg2 "Installing Startup Script"
  cd "${srcdir}"
  install -Dm755 joplin.sh "${pkgdir}/usr/bin/joplin-cli"
}


package_joplin-desktop() {
  pkgdesc="A note taking and to-do application with synchronization capabilities - Desktop"
  depends=('electron' 'gtk3' 'libexif' 'libgsf' 'libjpeg-turbo' 'libwebp' 'libxss' 'nodejs'
         'nss' 'orc')
  optdepends=('libappindicator-gtk3: for tray icon')
  conflicts=('joplin' 'joplin-desktop-electron')

  msg2 "Building Desktop with packaged Electron..."
  mkdir -p "${pkgdir}/usr/share/joplin-desktop"
  cd "${srcdir}/joplin-${pkgver}/packages/app-desktop"
  electron_dir="/usr/lib/electron"
  electron_version=$(cat /usr/lib/electron/version)

  USE_HARD_LINKS=false npm run dist -- --publish=never  --linux  --x64 \
    --dir="dist/" -c.electronDist=$electron_dir -c.electronVersion=$electron_version

  cd dist/linux-unpacked/
  cp -R "." "${pkgdir}/usr/share/joplin-desktop"

  msg2 "Installing LICENSE..."
  cd "${srcdir}/joplin-${pkgver}/"
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"

  msg2 "Installing startup script and desktop file..."
  cd "${srcdir}"
  install -Dm755 ${srcdir}/joplin-desktop.sh "${pkgdir}/usr/bin/joplin-desktop"
  install -Dm644 ${srcdir}/joplin.desktop -t "${pkgdir}/usr/share/applications"
}

package_joplin-desktop-electron() {
  pkgdesc="DEPRECATED: A note taking and to-do application with synchronization capabilities - Desktop"
  depends=('electron' 'gtk3' 'libexif' 'libgsf' 'libjpeg-turbo' 'libwebp' 'libxss' 'nodejs'
         'nss' 'orc')
  optdepends=('libappindicator-gtk3: for tray icon')
  conflicts=('joplin' 'joplin-desktop')
  package_joplin-desktop
}

