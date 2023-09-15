# Maintainer: Shatur95 <genaloner@gmail.com>
# Co-Maintainer: Mark Wagie <mark dot wagie at proton dot me>
# Contributor: ful1e5 <kaizmandhu at gmail dot com>

pkgname=bibata-cursor-theme
pkgver=2.0.4
pkgrel=1
pkgdesc="Material Based Cursor Theme"
arch=('any')
url="https://github.com/ful1e5/Bibata_Cursor"
license=('GPL3')
makedepends=('python-clickgen>=2.0.0')
options=('!strip')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz"
        "$pkgname-$pkgver-bitmaps.zip::$url/releases/download/v$pkgver/bitmaps.zip")
sha256sums=('88ee477d6e4a0be93ac0a5df6c5340a0643278c6b0e0ca8efc8c91c0de8e4f58'
            'c6f2e56e4d65fd4f009f70f564346410ba18985d9c03fbc55a0f0ee558dbc1c4')

prepare() {
  mv -f bitmaps "Bibata_Cursor-$pkgver"

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
