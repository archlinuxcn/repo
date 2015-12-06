# Maintainer: Ben Wolsieffer <benwolsieffer@gmail.com>

pkgname=wallch
_pkgname=wall-changer
pkgver=4.15
pkgrel=3
pkgdesc="A powerful general purpose wallpaper changer."
arch=('i686' 'x86_64')
url="http://melloristudio.com/wallch/"
license=('GPL3')
depends=('libexif' 'libkeybinder2' 'libnotify' 'libunity' 'libappindicator-gtk2' 'qt5-webkit' 'desktop-file-utils')
makedepends=('dee' 'sqlite' 'gst-plugins-base' 'libxslt' 'qt5-tools')
optdepends=('bash-completion: for bash auto-completion')
provides=('wallch')
source=("http://downloads.sourceforge.net/project/${_pkgname}/${pkgname}_${pkgver}.tar.gz")
install='wallch.install'
md5sums=('052eeeb70050444ec098a49a70e2987a')


build() {
	cd $srcdir/$pkgname-$pkgver 
	qmake-qt5 *.pro
	make
}

package() {
	cd $srcdir/$pkgname-$pkgver

	# Use correct lrelease binary
        sed -i -e 's|lrelease|lrelease-qt5|g' Makefile

	# Install
	make INSTALL_ROOT=${pkgdir} install
	install -Dm 755 wallch "${pkgdir}/usr/bin/wallch"

	# Install icon
	install -Dm644 data/pixmap/wallch.png "${pkgdir}/usr/share/pixmaps/wallch.png"

	# Install bash completion
	install -Dm 644 data/bash_autocompletion/wallch "${pkgdir}/usr/share/bash-completion/completions/wallch"

	# Install man page
	install -Dm 644 data/man/wallch.1.gz "${pkgdir}/usr/share/man/man1/wallch.1.gz"
}
