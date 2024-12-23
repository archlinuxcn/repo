# Maintainer: sem.z <sem.z at protonmail dot com>

pkgname="orca-slicer-bin"
pkgver=2.2.0
pkgrel=1
pkgdesc="G-code generator for 3D printers"
arch=('x86_64')
url="https://github.com/SoftFever/OrcaSlicer"
license=('AGPL3')
depends=('mesa' 'glu' 'gst-libav' 'gst-plugins-base' 'cairo' 'gtk3' 'libsoup' 'webkit2gtk' 'gstreamer' 'openvdb' 'wayland' 'wayland-protocols' 'libxkbcommon')
provides=("orca-slicer")
conflicts=("orca-slicer")
source=("https://github.com/SoftFever/OrcaSlicer/releases/download/v${pkgver}/OrcaSlicer_Linux_V${pkgver}.AppImage")
sha512sums=('0b17ad9a3efcfdd5ae97954329c9423863409345038025e99c6d6f920ed8e65df2bff8d685c070382cd3e0df4a764ce4304988c564763dabc0bc592294d1732b')

prepare() {
	chmod +x OrcaSlicer_Linux_V${pkgver}.AppImage
	./OrcaSlicer_Linux_V${pkgver}.AppImage --appimage-extract

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
