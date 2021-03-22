# Maintainer: Shatur95 <genaloner@gmail.com>
# Co-Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
# Contributor: ful1e5 <kaizmandhu at gmail dot com>

pkgname=bibata-cursor-theme
pkgver=1.1.0
pkgrel=4
pkgdesc="Material Based Cursor Theme"
arch=('any')
url="https://github.com/ful1e5/Bibata_Cursor"
license=('GPL3')
depends=('libxcursor' 'libpng')
makedepends=('python-clickgen')
options=('!strip')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz"
        "$pkgname-bitmaps-$pkgver.zip::$url/releases/download/v$pkgver/bitmaps.zip")
noextract=("$pkgname-bitmaps-$pkgver.zip")
sha256sums=('7b93fd3a06b7ec71731b611ee28ecaf04e48024453e3e774aed6612a97100ab1'
            '38f2a1e25d446dd81ef4693bf8401734d3200ad8237bbaa2f22c4036713a03ea')

prepare() {
  cd Bibata_Cursor-$pkgver
  mkdir -p bitmaps
  bsdtar -xf "$srcdir/$pkgname-bitmaps-$pkgver.zip" -C bitmaps

  rm -rf themes
}

build() {
  cd Bibata_Cursor-$pkgver/builder
  _themes='Amber Classic Ice'
  _sizes='22 24 28 32 40 48 56 64 72 80 88 96'

  set -- ${_sizes}
  for t in ${_themes}; do
    python build.py unix -p "../bitmaps/Bibata-Modern-$t" --xsizes ${_sizes[@]}
    python build.py unix -p "../bitmaps/Bibata-Original-$t" --xsizes ${_sizes[@]}
  done
}

package() {
  cd Bibata_Cursor-$pkgver
  install -d "$pkgdir"/usr/share/icons
  cp -r themes/Bibata-* "$pkgdir"/usr/share/icons
}
