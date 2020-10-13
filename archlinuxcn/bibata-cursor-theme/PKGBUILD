# Maintainer: Shatur95 <genaloner@gmail.com>
# Co-Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
# Contributor: ful1e5 <kaizmandhu at gmail dot com>

pkgname=bibata-cursor-theme
pkgver=1.0.1
pkgrel=2
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
sha256sums=('4764ffffbee14570bd2bb866f2e74e3957429343f99571219e0a120b89a5e81b'
            '8fd29627af316225437625271d608937f1015f8b169a200ec87118e69ff75c00')

prepare() {
  cd Bibata_Cursor-$pkgver
  mkdir -p bitmaps
  bsdtar -xf "$srcdir/$pkgname-bitmaps-$pkgver.zip" -C bitmaps

  rm -rf themes
}

build() {
  cd Bibata_Cursor-$pkgver
  python build.py --x11
}

package() {
  cd Bibata_Cursor-$pkgver
  install -d "$pkgdir"/usr/share/icons
  cp -r themes/Bibata-* "$pkgdir"/usr/share/icons
  chmod -R 755 "$pkgdir"/usr/share/icons/Bibata-*
}
