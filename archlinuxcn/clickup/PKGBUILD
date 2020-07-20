# Maintainer Xuanwo <xuanwo@archlinucn.org>
pkgname=clickup
pkgver=2.0.12
pkgrel=1
pkgdesc="Desktop app for clickup.com"
arch=('x86_64')
url="https://clickup.com"
license=('custom')
depends=('fuse2')
_dirname="$pkgname-desktop-$pkgver-linux"
_filename="$pkgname-desktop-$pkgver-x86_64.AppImage"
_downloadname="$pkgname-desktop-$pkgver-linux.zip"
options=('!strip')
source=("https://attachments3.clickup.com/desktop/$_downloadname")

prepare() {
  rm -rf squashfs-root
  chmod +x $_filename
  ./$_filename --appimage-extract
  sed -i -e "s|Exec=.\+|Exec=env APPIMAGELAUNCHER_DISABLE=1 DESKTOPINTEGRATION=0 /opt/$_filename|" squashfs-root/clickup-desktop.desktop
}

package() {
  install -Dm755 $_filename "$pkgdir/opt/$_filename"
  install -Dm644 squashfs-root/clickup-desktop.desktop "$pkgdir/usr/share/applications/clickup.desktop"
  install -dm755 "$pkgdir/usr/share/icons/hicolor"
  cp -av squashfs-root/usr/share/icons/hicolor/* "$pkgdir/usr/share/icons/hicolor/"
  chmod -R a+rX "$pkgdir/usr/share/icons/hicolor"
}
sha256sums=('a8dc26c26b6faf239c899d5633a6ab07116356505433de6b10dd9151da0c7783')
