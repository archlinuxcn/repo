
# Maintainer: Juanma Hernandez <juanmah@gmail.com>
# Contributor: Matthias Kurz <m.kurz@irregular.at>

pkgname=zotero-bin
pkgver=9.0.1
pkgrel=1
pkgdesc="Zotero Standalone. Is a free, easy-to-use tool to help you collect, organize, cite, and share your research sources."
arch=('x86_64' 'i686' 'aarch64')
url="https://www.zotero.org/download"
license=('AGPL-3.0-or-later')
depends=('alsa-lib' 'gtk3' 'nss')
provides=('zotero')
conflicts=('zotero')

sha256sums=('f727308716741cf9746b92047b890c3f76c4b8b010bc5ed21b5cdb1be85e21e9')
sha256sums_x86_64=('b8f07bb44270fac2b482e146e194cebb0f063e1b241ac74cd5a8df5832795ed4')
sha256sums_i686=('23cf0fad8b3b8425a6aed38d41aa336ed6985ba3c3c40a06a3c00247c3f194f3')
sha256sums_aarch64=('5ac3e381754d540671e52877cf685d2ddac4cfeb3e50e87f19a187ff8694d36e')
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
