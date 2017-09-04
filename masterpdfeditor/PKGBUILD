# Maintainer: Doug Newgard <scimmia at archlinux dot info>
# Contributor: Jiachen Yang <farseerfc@gmail.com>
# Contributor: Miguel Revilla <yo@miguelrevilla.com>
# Contributor: Ferik <djferik at gmail dot com>

pkgname=masterpdfeditor
pkgver=4.3.00
pkgrel=1
pkgdesc='A complete solution for creation and editing PDF files'
url='https://code-industry.net/free-pdf-editor/'
arch=('x86_64')
license=('custom')
makedepends=('patchelf')
source_x86_64=("http://get.code-industry.net/public/master-pdf-editor-${pkgver}_qt5.amd64.tar.gz")
sha1sums_x86_64=('aa7ac3ccc1aa71c3868267d324814deb6c05d57d')

package() {
  depends=('gcc-libs' 'glibc' 'libgl' 'qt5-base' 'qt5-svg' 'sane')

  install -d "$pkgdir"{/opt/,/usr/bin/}
  cp -a --no-preserve=ownership master-pdf-editor-${pkgver%%.*} "$pkgdir/opt/"
  ln -s /opt/master-pdf-editor-${pkgver%%.*}/masterpdfeditor${pkgver%%.*} -t "$pkgdir/usr/bin/"

  cd "$pkgdir/opt/master-pdf-editor-${pkgver%%.*}"
  install -Dm644 masterpdfeditor${pkgver%%.*}.desktop -t "$pkgdir/usr/share/applications/"
  install -Dm644 license.txt -t "$pkgdir/usr/share/licenses/$pkgname/"
  patchelf --remove-rpath masterpdfeditor${pkgver%%.*}
}
