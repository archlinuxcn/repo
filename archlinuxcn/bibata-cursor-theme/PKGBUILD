# Maintainer: Shatur95 <genaloner@gmail.com>
# Co-Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
# Contributor: ful1e5 <kaizmandhu at gmail dot com>

pkgname=bibata-cursor-theme
pkgver=1.1.1
pkgrel=1
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
sha256sums=('fb195e48cd9669ee915c038e5138acf39a5e2175696b95e94b3095d9c7847204'
            '9ec5b60c8de324f6ac732f17eb7c32ac4e5901df433703d746b9c13b45bb0479')

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
