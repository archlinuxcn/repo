# Maintainer: poscat

pkgname=lc3tools-electron-bin
pkgver=2.0.2
pkgrel=3
pkgdesc="LC3 emulator GUI"
arch=('x86_64' 'aarch64')
url='https://github.com/chiragsakhuja/lc3tools'
license=('Apache 2.0')
source=(
  "${url}/releases/download/v${pkgver}/LC3Tools-${pkgver}.AppImage"
)
sha256sums=('410b352109bf54f9e8260c34f9cbb67ab7e4eec3877bff9b913f459b716e57f4')
options=(!debug)

prepare() {
  AppImage="$srcdir/LC3Tools-${pkgver}.AppImage"
  chmod +x "$AppImage"
  "$AppImage" --appimage-extract

  sed -i 's|Exec=AppRun|Exec=/opt/lc3tools/lc3tools|g' squashfs-root/lc3tools.desktop

  find squashfs-root/{resources,usr/share/icons} -type d -exec chmod 755 {} +
}

package() {
  install -d "$pkgdir/opt/lc3tools"
  cp -av squashfs-root/* "$pkgdir/opt/lc3tools"

  install -d "$pkgdir/usr/share/icons"
  mv "$pkgdir"/opt/lc3tools/usr/share/icons/hicolor "$pkgdir"/usr/share/icons

  install -d "$pkgdir/usr/share/applications"
  mv "$pkgdir"/opt/lc3tools/lc3tools.desktop "$pkgdir"/usr/share/applications

  rm -rf "$pkgdir/opt/lc3tools/usr"
  rm "$pkgdir"/opt/lc3tools/{AppRun,lc3tools.png}
}
