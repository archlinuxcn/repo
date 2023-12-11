# Maintainer: Bryce Kabat <brycekabat@onyxazryn.com>
pkgname="trilium-bin"
pkgver=0.62.4
pkgrel=2
pkgdesc="A hierarchical note taking application built on modern technologies."
depends=('libxss' 'nss' 'gtk3' 'alsa-lib')
arch=('x86_64')
url="https://github.com/zadam/trilium"
license=('AGPL3')
source=("https://github.com/zadam/trilium/releases/download/v$pkgver/trilium-linux-x64-$pkgver.tar.xz")
sha512sums=('24ef459b9419cae30911d9e388f59a5e2daedadb227bb89b84462b8037f585344786610ef77b83af187a6fc847f8bc9c0bd796f22d1e570388bef61b6dfcd0f2')

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
