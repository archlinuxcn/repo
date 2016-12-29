# Maintainer: Jiachen Yang <farseerfc@gmail.com>
# Contributor: Arthur Zamarin <arthurzam@gmail.com>
# Contributor: Ferik <djferik at gmail dot com>
# Contributor for Qt5 version: pavbaranov

pkgname=masterpdfeditor-qt5
pkgver=3.7.10
pkgrel=2
pkgdesc="A complete solution for creation and editing PDF files. (Free for non-commercial use) - Qt5 version"
url="http://code-industry.net/free-pdf-editor.php"
arch=('x86_64')
license=('custom')
depends=('qt5-base' 'qt5-svg')
conflicts=('masterpdfeditor')

source=(${pkgname}.desktop)
source_x86_64=(http://get.code-industry.net/public/master-pdf-editor-${pkgver}_qt5.amd64.tar.gz)

sha256sums=('29218c206e5b78776bc3ec44a760773273274bb56baee5e19e06c3ec55db59fd')
sha256sums_x86_64=('361f75e278574c6397bdec0ed122efb16287798f9f2cc42056ce1808a963707b')

package() {
    mkdir -p "${pkgdir}/opt/masterpdfeditor"
    cd "${srcdir}/master-pdf-editor-3"
    /bin/tar cf - * | ( cd "${pkgdir}"/opt/masterpdfeditor; tar xfp - )
    install -D -m755 "${srcdir}"/master-pdf-editor-3/lang/*.qm "${pkgdir}"/opt/masterpdfeditor/lang
    install -D -m755 "${srcdir}"/master-pdf-editor-3/lang/*.ts "${pkgdir}"/opt/masterpdfeditor/lang
    install -D -m644 "${srcdir}"/master-pdf-editor-3/license.txt "${pkgdir}"/usr/share/licenses/${pkgname}/LICENSE
    install -D -m644 "${srcdir}"/master-pdf-editor-3/masterpdfeditor3.png "${pkgdir}"/usr/share/pixmaps/pdfeditor.png
    install -D -m644 "${srcdir}"/masterpdfeditor-qt5.desktop "${pkgdir}"/usr/share/applications/masterpdfeditor.desktop
    rm "${pkgdir}"/opt/masterpdfeditor/license.txt
    chmod 644 "${pkgdir}"/opt/masterpdfeditor/lang/*
    chmod 755 "${pkgdir}"/opt/masterpdfeditor/lang
    mkdir -p "${pkgdir}"/usr/bin
    ln -s /opt/masterpdfeditor/masterpdfeditor3 "${pkgdir}"/usr/bin/pdfeditor
}
