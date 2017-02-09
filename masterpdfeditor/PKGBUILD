# Maintainer: Doug Newgard <scimmia at archlinux dot info>
# Contributor: Jiachen Yang <farseerfc@gmail.com>
# Contributor: Miguel Revilla <yo@miguelrevilla.com>
# Contributor: Ferik <djferik at gmail dot com>

pkgname=masterpdfeditor
pkgver=4.0.40
pkgrel=1
pkgdesc='A complete solution for creation and editing PDF files'
url='http://code-industry.net/free-pdf-editor.php'
arch=('x86_64')
license=('custom')
makedepends=('patchelf')
source=('masterpdfeditor.desktop')
source_x86_64=("http://get.code-industry.net/public/master-pdf-editor-${pkgver}_qt5.amd64.tar.gz")
sha1sums=('5b3a0392390e49d4f7f4e478dd336476436f5cfa')
sha1sums_x86_64=('9184a39253edade7b2f9d92aae0a674cb976043f')

package() {
  depends=('qt5-base' 'qt5-svg' 'sane')

  install -d "$pkgdir"{/opt/,/usr/bin/,/usr/share/applications/}
  cp -a --no-preserve=ownership master-pdf-editor-${pkgver%%.*} "$pkgdir/opt/"
  sed "s/VERMAJ/${pkgver%%.*}/g" masterpdfeditor.desktop > "$pkgdir/usr/share/applications/masterpdfeditor${pkgver%%.*}.desktop"
  ln -s /opt/master-pdf-editor-${pkgver%%.*}/masterpdfeditor${pkgver%%.*} -t "$pkgdir/usr/bin/"
  install -Dm644 master-pdf-editor-${pkgver%%.*}/license.txt -t "$pkgdir/usr/share/licenses/$pkgname/"
  patchelf --remove-rpath "$pkgdir/opt/master-pdf-editor-${pkgver%%.*}/masterpdfeditor${pkgver%%.*}"
}
