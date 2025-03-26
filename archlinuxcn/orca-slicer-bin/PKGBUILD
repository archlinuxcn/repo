# Maintainer: Poscat
# Contributor: sem.z <sem.z at protonmail dot com>

pkgname="orca-slicer-bin"
pkgver=2.3.0
pkgrel=2
pkgdesc="G-code generator for 3D printers"
arch=('x86_64')
url="https://github.com/SoftFever/OrcaSlicer"
license=('AGPL3')
depends=('mesa' 'glu' 'gst-libav' 'gst-plugins-base' 'cairo' 'gtk3' 'libsoup' 'webkit2gtk' 'gstreamer' 'openvdb' 'wayland' 'wayland-protocols' 'libxkbcommon' 'webkit2gtk-4.1')
provides=("orca-slicer")
conflicts=("orca-slicer")
appimage="OrcaSlicer_Linux_AppImage_Ubuntu2404_V${pkgver}.AppImage"
source=("https://github.com/SoftFever/OrcaSlicer/releases/download/v${pkgver}/${appimage}")
sha512sums=('2a9def84723f8d362d0c29b1618d045a49e2f0b4008f351e1174c8f699154a84386bc6f31aa1f095391a43613f84a5d1308c2bb125b4530219c24580c83667f2')

prepare() {
  chmod +x ${appimage}
  ./${appimage} --appimage-extract

  sed -i 's|Exec=AppRun|Exec=/opt/orca-slicer/bin/orca-slicer|g' \
    "squashfs-root/OrcaSlicer.desktop"
}

package() {
  find squashfs-root/{resources,usr/share/icons}/ -type d -exec chmod 755 {} +

  install -d "$pkgdir/opt/${pkgname%-bin}/"
  cp -av squashfs-root/* "$pkgdir/opt/${pkgname%-bin}/"
  rm -rf "$pkgdir/opt/${pkgname%-bin}/usr/"
  rm "$pkgdir/opt/${pkgname%-bin}"/{OrcaSlicer.desktop,AppRun,OrcaSlicer.png,OrcaSlicer-x86_64.AppImage}

  install -d "$pkgdir/usr/bin"
  ln -s "/opt/${pkgname%-bin}/bin/orca-slicer" "$pkgdir/usr/bin/"

  install -Dm644 "squashfs-root/OrcaSlicer.desktop" -t \
    "$pkgdir/usr/share/applications/"

  install -d "$pkgdir/usr/share/icons/"
  cp -r squashfs-root/usr/share/icons/hicolor/ "$pkgdir/usr/share/icons/"
}
