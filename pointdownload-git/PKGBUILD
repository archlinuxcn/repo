# Maintainer: Stephen Zhang <zsrkmyn at gmail dot com>
pkgname=pointdownload-git
pkgver=r155.82baa70
pkgrel=1
pkgdesc="A downloader supporting http, ftp, bt, magnet and thunder protocol"
arch=('x86_64' 'i686')
url="https://github.com/PointTeam/PointDownload"
license=('GPL3')
depends=('gcc-libs' 'qt5-base' 'qt5-webkit' 'qt5-declarative' 'qt5-multimedia' 'qt5-graphicaleffects')
makedepends=('git')
conflicts=('pointdownload')
provides=('pointdownload')
install=pointdownload.install
source=('git://github.com/PointTeam/PointDownload#branch=develop')
md5sums=('SKIP')

pkgver() {
	cd "$srcdir/PointDownload"
	printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
	cd $srcdir/PointDownload
	qmake-qt5
	make
}

package() {
	cd $srcdir/PointDownload
	INSTALL_ROOT=$pkgdir/ make install
	install -d $pkgdir/usr/share/applications
	install -Dm644 pointpopup.desktop $pkgdir/usr/share/applications
	install -Dm644 pointdownload.desktop $pkgdir/usr/share/applications

	cd $pkgdir

	install -d $pkgdir/usr/bin

	cat > $pkgdir/usr/bin/pointdownload <<"EOF"
#!/bin/sh
/opt/Point/PointDownload/PointDownload $@
EOF

	chmod +x $pkgdir/usr/bin/pointdownload
}
