# Maintainer: Juanma Hernandez <juanmah@gmail.com>

pkgname=zotero-bin
pkgver=6.0.20
pkgrel=1
pkgdesc="Zotero Standalone. Is a free, easy-to-use tool to help you collect, organize, cite, and share your research sources."
arch=('x86_64')
url="https://www.zotero.org/download"
license=('AGPL3')
depends=('dbus-glib' 'gtk3' 'nss' 'libxt')
provides=('zotero')
conflicts=('zotero')
replaces=('zotero')

sha256sums=('eab76db7a56a4d9aaa17baaf240b82fcf57944a4ddf8ef1b58cc64182426cedc')
sha256sums_x86_64=('1ec02fa1daa2a37189f532b5a6de16c25119100a39da8707d2bedc7fd2107bdc')

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
  # No need to keep a shell around when launching Zotero
  sed -i -r 's/^("\$CALLDIR\/zotero-bin" -app "\$CALLDIR\/application.ini" "\$@")/exec \1/' "$pkgdir"/usr/lib/zotero/zotero
}
