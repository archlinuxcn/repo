# Maintainer: Miguel Revilla <yo@miguelrevilla.com>
# Contributor: Ferik <djferik at gmail dot com>

pkgname=masterpdfeditor
pkgver=3.5.10
pkgrel=1
pkgdesc="A complete solution for creation and editing PDF files. (Free for non-commercial use)"
url="http://code-industry.net/free-pdf-editor.php"
arch=('i686' 'x86_64')
license=('custom')
depends=('qt4')
install=${pkgname}.install

source=(${pkgname}.desktop)
source_i686=(http://get.code-industry.net/public/master-pdf-editor-${pkgver}_i386.tar.gz)
source_x86_64=(http://get.code-industry.net/public/master-pdf-editor-${pkgver}_amd64.tar.gz)

sha256sums=('29218c206e5b78776bc3ec44a760773273274bb56baee5e19e06c3ec55db59fd')
sha256sums_i686=('c6c2a4a977d76492cb9f607caa0c472bab98e70bc187151f006fb7af4f885bbf')
sha256sums_x86_64=('1a3b7c0429293f99f7e25ae3fe622bd0074e0a49c2d1eaecc9a1879e0261c894')

package() {
	mkdir -p "${pkgdir}/opt/masterpdfeditor"
	cd "${srcdir}/master-pdf-editor-3"
	/bin/tar cf - * | ( cd "${pkgdir}"/opt/masterpdfeditor; tar xfp - )
	install -D -m755 "${srcdir}"/master-pdf-editor-3/lang/*.qm "${pkgdir}"/opt/masterpdfeditor/lang
	install -D -m755 "${srcdir}"/master-pdf-editor-3/lang/*.ts "${pkgdir}"/opt/masterpdfeditor/lang
	install -D -m644 "${srcdir}"/master-pdf-editor-3/license.txt "${pkgdir}"/usr/share/licenses/masterpdfeditor/LICENSE
	install -D -m644 "${srcdir}"/master-pdf-editor-3/masterpdfeditor3.png "${pkgdir}"/usr/share/pixmaps/pdfeditor.png
	install -D -m644 "${srcdir}"/masterpdfeditor.desktop "${pkgdir}"/usr/share/applications/masterpdfeditor.desktop
	rm "${pkgdir}"/opt/masterpdfeditor/license.txt
	chmod 644 "${pkgdir}"/opt/masterpdfeditor/lang/*
	chmod 755 "${pkgdir}"/opt/masterpdfeditor/lang
	mkdir -p "${pkgdir}"/usr/bin
	ln -s /opt/masterpdfeditor/masterpdfeditor3 "${pkgdir}"/usr/bin/pdfeditor
}
