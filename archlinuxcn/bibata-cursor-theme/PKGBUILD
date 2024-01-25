# Maintainer: Shatur95 <genaloner@gmail.com>
# Co-Maintainer: Mark Wagie <mark dot wagie at proton dot me>
# Contributor: ful1e5 <kaizmandhu at gmail dot com>

pkgname=bibata-cursor-theme
pkgver=2.0.6
pkgrel=1
pkgdesc="Material Based Cursor Theme"
arch=('any')
url="https://github.com/ful1e5/Bibata_Cursor"
license=('GPL-3.0-or-later')
makedepends=('python-clickgen>=2.0.0')
options=('!strip')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz"
        "$pkgname-$pkgver-bitmaps.zip::$url/releases/download/v$pkgver/bitmaps.zip")
noextract=("$pkgname-$pkgver-bitmaps.zip")
sha256sums=('a3095d6a49c2fef1f97963d3706cfcf19b2f29c0616f423f5a278714b60f2b19'
            '651fd17ceec14ef1c148a32a96b83902e6a7f334396feca39f5eb15a7e1fef22')

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
