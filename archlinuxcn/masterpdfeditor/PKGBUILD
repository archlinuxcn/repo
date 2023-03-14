# Maintainer: Patrick Goetz <pgoetz at mail dot utexas dot edu>
# Contributor: Doug Newgard <scimmia at archlinux dot org>
# Contributor: Jiachen Yang <farseerfc@gmail.com>
# Contributor: Miguel Revilla <yo@miguelrevilla.com>
# Contributor: Ferik <djferik at gmail dot com>

pkgname=masterpdfeditor
pkgver=5.9.40
pkgrel=4
pkgdesc='A complete solution for viewing, creating and editing PDF files'
url='https://code-industry.net/free-pdf-editor/'
arch=('x86_64')
license=('custom')
makedepends=('patchelf')
source_x86_64=("https://code-industry.net/public/master-pdf-editor-${pkgver}-qt5.x86_64.tar.gz"
               masterpdfeditor5.desktop
               license.txt)
sha1sums_x86_64=('9207e438dc8fd08e4ee1d99d80576134b3f720bc'
                 'b33e7148123565fd4cc15d41c493f6ab27d37ba4'
                 '75ab655977f493aa46fd3aa6cb1cbfcf19b40d97')

package() {
  depends=('libgl' 'nspr' 'nss' 'qt5-base' 'qt5-svg' 'qt5-declarative' 'sane')

  install -d "$pkgdir"{/opt/,/usr/bin/}
  cp -a --no-preserve=ownership master-pdf-editor-${pkgver%%.*} "$pkgdir/opt/"

  cd "$pkgdir/opt/master-pdf-editor-${pkgver%%.*}"
  ln -sr masterpdfeditor${pkgver%%.*} -t "$pkgdir/usr/bin/"
  install -Dm644 ${srcdir}/masterpdfeditor${pkgver%%.*}.desktop -t "$pkgdir/usr/share/applications/"
  install -Dm644 ${srcdir}/license.txt -t "$pkgdir/usr/share/licenses/$pkgname/"
  patchelf --remove-rpath masterpdfeditor${pkgver%%.*}
}
