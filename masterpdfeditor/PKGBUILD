# Maintainer: Miguel Revilla <yo@miguelrevilla.com>
# Contributor: Ferik <djferik at gmail dot com>

pkgname=masterpdfeditor
pkgver=3.3.00
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
sha256sums_i686=('b27661f843c5771a79aeae38013ceee87343701fc89a0a4386fd9b08cbe266d1')
sha256sums_x86_64=('2bd562ce95189b6b474ab41806452c44cf4fe3bbb1df3b5571abe35a977b9d65')

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
