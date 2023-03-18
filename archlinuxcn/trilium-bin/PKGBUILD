# Maintainer: Bryce Kabat <brycekabat@onyxazryn.com>
pkgname="trilium-bin"
pkgver=0.59.2
pkgrel=1
pkgdesc="A hierarchical note taking application built on modern technologies."
depends=('libxss' 'nss' 'gtk3')
arch=('x86_64')
url="https://github.com/zadam/trilium"
license=('AGPL3')
source=("https://github.com/zadam/trilium/releases/download/v$pkgver/trilium-linux-x64-$pkgver.tar.xz")
sha512sums=('0739eaff88450e979dc74c02b57993ca50b82124e922638c2191f4f88b494bad227cfd06c5ffe252c7eb7991e16bf404c3a0456c3080417ac8ce9f03d87f1dde')

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
