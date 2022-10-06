# Maintainer: Shatur95 <genaloner@gmail.com>
# Co-Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
# Contributor: ful1e5 <kaizmandhu at gmail dot com>

pkgname=bibata-cursor-theme
pkgver=2.0.1
pkgrel=1
pkgdesc="Material Based Cursor Theme"
arch=('any')
url="https://github.com/ful1e5/Bibata_Cursor"
license=('GPL3')
makedepends=('python-clickgen>=2.0.0')
options=('!strip')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('2f1f093e422f38467f7dc3726062c63c78c8197a2e1472642d54e7580a7e6f14')

prepare() {
  cd Bibata_Cursor-$pkgver
  rm -rf themes
}

build() {
  cd Bibata_Cursor-$pkgver
  echo "Building 'Bibata Modern Amber' Cursors"
  ctgen build.toml -p 'x11' -n 'Bibata-Modern-Amber' \
    -c 'Yellowish and rounded edge Bibata cursors.' \
    -d 'bitmaps/Bibata-Modern-Amber'

  echo "Building 'Bibata Original Amber' Cursors"
  ctgen build.toml -p 'x11' -n 'Bibata-Original-Amber' \
    -c 'Yellowish and sharp edge Bibata cursors.' \
    -d 'bitmaps/Bibata-Original-Amber'

  echo "Building 'Bibata Modern Classic' Cursors"
  ctgen build.toml -p 'x11' -n 'Bibata-Modern-Classic' \
    -c 'Black and rounded edge Bibata cursors.' \
    -d 'bitmaps/Bibata-Modern-Classic'

  echo "Building 'Bibata Original Classic' Cursors"
  ctgen build.toml -p 'x11' -n 'Bibata-Original-Classic' \
    -c 'Black and sharp edge Bibata cursors.' \
    -d 'bitmaps/Bibata-Original-Classic'

  echo "Building 'Bibata Modern Ice' Cursors"
  ctgen build.toml -p 'x11' -n 'Bibata-Modern-Ice' \
    -c 'White and rounded edge Bibata cursors.' \
    -d 'bitmaps/Bibata-Modern-Ice'

  echo "Building 'Bibata Original Ice' Cursors"
  ctgen build.toml -p 'x11' -n 'Bibata-Original-Ice' \
    -c 'White and sharp edge bibata cursors.' \
    -d 'bitmaps/Bibata-Original-Ice'
}

package() {
  cd Bibata_Cursor-$pkgver
  install -d "$pkgdir"/usr/share/icons
  cp -r themes/Bibata-* "$pkgdir"/usr/share/icons/
}
