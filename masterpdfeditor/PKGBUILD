# Maintainer: Miguel Revilla <yo@miguelrevilla.com>
# Contributor: Ferik <djferik at gmail dot com>

pkgname=masterpdfeditor
pkgver=3.4.10
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
sha256sums_i686=('2cff1c0b23ab7c78cb0cda54823094d5f87c6edded6b97c9920995233c8a4387')
sha256sums_x86_64=('c2f17ab43cbcfcb6566c3d418e118ac78fb09a979c4a85439b35b628f5141cce')

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
