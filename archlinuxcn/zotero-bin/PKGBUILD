
# Maintainer: Juanma Hernandez <juanmah@gmail.com>
# Contributor: Matthias Kurz <m.kurz@irregular.at>

pkgname=zotero-bin
pkgver=9.0
pkgrel=1
pkgdesc="Zotero Standalone. Is a free, easy-to-use tool to help you collect, organize, cite, and share your research sources."
arch=('x86_64' 'i686' 'aarch64')
url="https://www.zotero.org/download"
license=('AGPL-3.0-or-later')
depends=('alsa-lib' 'gtk3' 'nss')
provides=('zotero')
conflicts=('zotero')

sha256sums=('f727308716741cf9746b92047b890c3f76c4b8b010bc5ed21b5cdb1be85e21e9')
sha256sums_x86_64=('897eea5f586a86c8d06b5b3b48be7d8a01ce690f2b0f9df2c9c025e5bcdba1cb')
sha256sums_i686=('bdd926330883d35bd0b32e689dd8044a9c6dc7e6394e344dd3a6e60d701bd127')
sha256sums_aarch64=('d01f4c49e67f3be6fe348cd869bea685dd231867dd5cbb33a0fc4f00c536c35d')
source=("zotero.desktop")
source_x86_64=("Zotero-${pkgver}_linux_x86_64.tar.bz2::https://www.zotero.org/download/client/dl?channel=release&platform=linux-x86_64&version=${pkgver}")
source_i686=("Zotero-${pkgver}_linux_i686.tar.bz2::https://www.zotero.org/download/client/dl?channel=release&platform=linux-i686&version=${pkgver}")
source_aarch64=("Zotero-${pkgver}_linux_arm64.tar.bz2::https://www.zotero.org/download/client/dl?channel=release&platform=linux-arm64&version=${pkgver}")

prepare() {
  if [[ "$CARCH" == "aarch64" ]]; then
    mv ${srcdir}/Zotero_linux-arm64 ${srcdir}/Zotero_linux-aarch64
  fi
}

package() {
  install -dDm755 "$pkgdir"/usr/{bin,lib/zotero}
  mv "$srcdir"/Zotero_linux-$CARCH/* "$pkgdir"/usr/lib/zotero
  ln -s /usr/lib/zotero/zotero "$pkgdir"/usr/bin/zotero
  install -Dm644 "$srcdir"/zotero.desktop "$pkgdir"/usr/share/applications/zotero.desktop
  # Copy zotero icons to a standard location
  install -Dm644 "$pkgdir"/usr/lib/zotero/icons/icon32.png "$pkgdir"/usr/share/icons/hicolor/32x32/apps/zotero.png
  install -Dm644 "$pkgdir"/usr/lib/zotero/icons/icon64.png "$pkgdir"/usr/share/icons/hicolor/64x64/apps/zotero.png
  install -Dm644 "$pkgdir"/usr/lib/zotero/icons/icon128.png "$pkgdir"/usr/share/icons/hicolor/128x128/apps/zotero.png
  install -Dm644 "$pkgdir"/usr/lib/zotero/icons/symbolic.svg "$pkgdir"/usr/share/icons/hicolor/symbolic/apps/zotero-symbolic.svg
  # No need to keep a shell around when launching Zotero
  sed -i -r 's/^("\$CALLDIR\/zotero-bin" -app "\$CALLDIR\/application.ini" "\$@")/exec \1/' "$pkgdir"/usr/lib/zotero/zotero
}
