# Maintainer: Bryce Kabat <brycekabat@onyxazryn.com>
pkgname="trilium-bin"
pkgver=0.61.14
pkgrel=2
pkgdesc="A hierarchical note taking application built on modern technologies."
depends=('libxss' 'nss' 'gtk3' 'alsa-lib')
arch=('x86_64')
url="https://github.com/zadam/trilium"
license=('AGPL3')
source=("https://github.com/zadam/trilium/releases/download/v$pkgver/trilium-linux-x64-$pkgver.tar.xz")
sha512sums=('7f6ded69fdf81da08e4cb4faac215e0ac856a4989d3a1f46e7c7fbfed6a0ade87d8263ac3914544c3fe3658b80e27fc0aee29bda5b62c45e2fd56b8ab3d55261')

package()
{
	export destdir="$pkgdir/"
	# Make folders for extraction
	mkdir -p "$pkgdir/opt/$pkgname"
	mkdir -p "$pkgdir/usr/bin"
	mkdir -p "$pkgdir/usr/share/applications"
	# Move main files
	mv trilium-linux-x64/* "$pkgdir/opt/$pkgname"
	# Write command and make executable
	echo -e "#!/bin/sh
/opt/$pkgname/trilium" > "$pkgdir/usr/bin/trilium"
	# Create .desktop file
	echo -e "[Desktop Entry]
Name=Trilium
GenericName=Note Taking Application
Comment=A hierarchical note taking application built on modern technologies.
Exec=trilium %f
Icon=/opt/$pkgname/icon.png
Terminal=false
Type=Application
Categories=Office
StartupWMClass=trilium notes" > "$pkgdir/usr/share/applications/trilium-notes.desktop"
	chmod -R 0755 "$pkgdir"
}
