# Maintainer: Blessing-Studio
# Contributor: mail_set
pkgname=wonderlab
pkgver=1.0.1.4
pkgrel=1
pkgdesc="下一代跨平台 Minecraft 启动器"
arch=('x86_64')
url="https://github.com/Blessing-Studio/WonderLab"
license=('MIT')
depends=('dotnet-runtime-6.0')
options=('!strip' '!emptydirs')
source=("https://github.com/Blessing-Studio/WonderLab/releases/download/${pkgver}/linux-${arch}.deb")
sha512sums=('SKIP')

package(){

	# Extract package data
	tar -xJ -f data.tar.xz -C "${pkgdir}"

	# Fix directory structure differences
	cd "${pkgdir}"

	mkdir usr/bin 2> /dev/null; mv usr/local/bin/* usr/bin; rm -rf usr/local/bin
	ls usr/share/applications/*.desktop | while read line; do
	sed -i s'/^Exec=\/usr\/local\/bin\//Exec=\/usr\/bin\//g' "$line"
	done

	rm -rf usr/local

	cd ..

}
