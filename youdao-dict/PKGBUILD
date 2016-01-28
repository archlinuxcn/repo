# Maintainer: yesuu zhang <yesuu79@qq.com>

pkgname=youdao-dict
pkgver=1.1.0
pkgrel=1
pkgdesc='YouDao Dictionary'
arch=('i686' 'x86_64')
url='http://cidian.youdao.com/index-linux.html'
license=('GPL3')
depends=(
	'desktop-file-utils'
	'hicolor-icon-theme'
	'python'
	'python-pyqt5'
	'python-requests'
	'python-xlib'
	'python-pillow'
	'tesseract-data-eng'
	'tesseract-data-chi_tra'
	'tesseract-data-chi_sim'
	'python-lxml'
	'python-xdg'
	'python-webob'
	'qt5-webkit'
)
install=youdao-dict.install
source_i686=('http://codown.youdao.com/cidian/linux/youdao-dict_1.1.0-0~i386.tar.gz')
source_x86_64=('http://codown.youdao.com/cidian/linux/youdao-dict_1.1.0-0~amd64.tar.gz')
sha256sums_i686=('d1ff404f1e465d6a196b566294ddfea1a1bfe4568226201b65d74236407152fc')
sha256sums_x86_64=('5c3a5ed105238e2fad181704fd99815c4275bf546136f99e817614188794dc07')

package() {
	cd "${srcdir}"
	mkdir -p "${pkgdir}/usr/bin"
	mkdir -p "${pkgdir}/usr/share/youdao-dict"
	mkdir -p "${pkgdir}/usr/share/applications"
	mkdir -p "${pkgdir}/usr/share/dbus-1/services"
	mkdir -p "${pkgdir}/usr/share/icons/hicolor/48x48/apps"
	mkdir -p "${pkgdir}/usr/share/icons/hicolor/scalable/apps"
	mkdir -p "${pkgdir}/etc/xdg/autostart"
	cp -r src/* "${pkgdir}/usr/share/youdao-dict"
	cp -r data/hicolor/* "${pkgdir}/usr/share/icons/hicolor/"
	cp data/youdao-dict.desktop "${pkgdir}/usr/share/applications/"
	cp data/youdao-dict-autostart.desktop "${pkgdir}/etc/xdg/autostart/"
	cp data/com.youdao.backend.service "${pkgdir}/usr/share/dbus-1/services/"
	chmod 755 "${pkgdir}/usr/share/youdao-dict/main.py"
	chmod 755 "${pkgdir}/usr/share/youdao-dict/youdao-dict-backend.py"
	ln -sf /usr/share/youdao-dict/main.py "${pkgdir}/usr/bin/youdao-dict"
}

