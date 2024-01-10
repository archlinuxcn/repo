# Maintainer: Shatur95 <genaloner@gmail.com>
# Co-Maintainer: Mark Wagie <mark dot wagie at proton dot me>
# Contributor: ful1e5 <kaizmandhu at gmail dot com>

pkgname=bibata-cursor-theme
pkgver=2.0.5
pkgrel=1
pkgdesc="Material Based Cursor Theme"
arch=('any')
url="https://github.com/ful1e5/Bibata_Cursor"
license=('GPL3')
makedepends=('python-clickgen>=2.0.0')
options=('!strip')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz"
        "$pkgname-$pkgver-bitmaps.zip::$url/releases/download/v$pkgver/bitmaps.zip")
noextract=("$pkgname-$pkgver-bitmaps.zip")
sha256sums=('deb4e2598ffedf21e96d961fccdc653236eb6c8c32e5b05dcfdb49563d4c93cf'
            '0fd1c0eef4b52eaadca6611f69c0fa1abe2756be02bf163666f361544af3b67f')

prepare() {
  bsdtar xvf "$pkgname-$pkgver-bitmaps.zip" -C "Bibata_Cursor-$pkgver"

  cd "Bibata_Cursor-$pkgver"
  rm -rf themes
}

build() {
  cd "Bibata_Cursor-$pkgver"

  declare -A names
  names["Bibata-Modern-Amber"]="Yellowish and rounded edge Bibata cursors."
  names["Bibata-Modern-Classic"]="Black and rounded edge Bibata cursors."
  names["Bibata-Modern-Ice"]="White and rounded edge Bibata cursors."
  names["Bibata-Original-Amber"]="Yellowish and sharp edge Bibata cursors."
  names["Bibata-Original-Classic"]="Black and sharp edge Bibata cursors."
  names["Bibata-Original-Ice"]="White and sharp edge Bibata cursors."

  for key in "${!names[@]}"; do
    comment="${names[$key]}"
    ctgen build.toml -p x11 -d "bitmaps/$key" -n "$key" -c "$comment" &
    PID=$!
    wait $PID
  done
}

package() {
  cd "Bibata_Cursor-$pkgver"
  install -d "$pkgdir/usr/share/icons"
  cp -r themes/Bibata-* "$pkgdir/usr/share/icons/"
}
