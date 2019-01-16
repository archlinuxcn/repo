# Contributor: Juanma Hernandez <juanmah@gmail.com>
# Maintainer: Juanma Hernandez <juanmah@gmail.com>

pkgname=zotero
pkgver=5.0.59
pkgrel=1
pkgdesc="Zotero Standalone. Is a free, easy-to-use tool to help you collect, organize, cite, and share your research sources."
arch=('x86_64')
url="http://www.zotero.org/download"
license=('GPL3')
depends=('dbus-glib' 'gtk2' 'gtk3' 'nss' 'libxt')

sha256sums=('2e700ebe97d332a894be80d232b037b0117d84b38c5fa99dffc727cb10918228')
sha256sums_x86_64=('ca60a989a062d7edf0e40a0fc90e41428dcafd3bfc81a59b0a479b9abccc2f00')

install='zotero.install'

source=("zotero.desktop")
source_x86_64=("Zotero-${pkgver}_linux_$CARCH.tar.bz2::https://www.zotero.org/download/client/dl?channel=release&platform=linux-$CARCH&version=${pkgver}")
        
package() {
  install -dDm755 "$pkgdir"/usr/{bin,lib/zotero}
  mv "$srcdir"/Zotero_linux-$CARCH/* "$pkgdir"/usr/lib/zotero
  ln -s /usr/lib/zotero/zotero "$pkgdir"/usr/bin/zotero
  install -Dm644 "$srcdir"/zotero.desktop "$pkgdir"/usr/share/applications/zotero.desktop
  # Copy zotero icons to a standard location
  install -Dm644 "$pkgdir"/usr/lib/zotero/chrome/icons/default/default16.png "$pkgdir"/usr/share/icons/hicolor/16x16/apps/zotero.png
  install -Dm644 "$pkgdir"/usr/lib/zotero/chrome/icons/default/default32.png "$pkgdir"/usr/share/icons/hicolor/32x32/apps/zotero.png
  install -Dm644 "$pkgdir"/usr/lib/zotero/chrome/icons/default/default48.png "$pkgdir"/usr/share/icons/hicolor/48x48/apps/zotero.png
  install -Dm644 "$pkgdir"/usr/lib/zotero/chrome/icons/default/default256.png "$pkgdir"/usr/share/icons/hicolor/256x256/apps/zotero.png
  # Disable APP update
  sed -i '/pref("app.update.enabled", true);/c\pref("app.update.enabled", false);' "$pkgdir"/usr/lib/zotero/defaults/preferences/prefs.js
}
