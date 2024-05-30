# Maintainer: Bryce Kabat <brycekabat@onyxazryn.com>
# Maintainer: Kevin Leutzinger <thedookmaster@gmail.com>
pkgname="trilium-bin"
pkgver=0.63.7
pkgrel=1
pkgdesc="A hierarchical note taking application built on modern technologies."
depends=('libxss' 'nss' 'gtk3' 'alsa-lib')
arch=('x86_64')
url="https://github.com/zadam/trilium"
license=('AGPL3')
source=("https://github.com/zadam/trilium/releases/download/v$pkgver/trilium-linux-x64-$pkgver.tar.xz")
sha512sums=('ce54fcc6c19a7395d2de9b6c366ae5ffd9a6481f23cbe4a6fd09f5ac5fb398bf64a2e8c61f73ab155fe0a907a885f4040cc73ba37876737ea66f400ffbe717eb')

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
