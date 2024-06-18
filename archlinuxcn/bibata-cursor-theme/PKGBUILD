# Maintainer: Shatur95 <genaloner@gmail.com>
# Co-Maintainer: Mark Wagie <mark dot wagie at proton dot me>
# Contributor: ful1e5 <kaizmandhu at gmail dot com>

pkgname=bibata-cursor-theme
pkgver=2.0.7
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
sha256sums=('1f21e5cade53d668476f973bd8ec827882a0e32c38e0e766abf007f8b3b46313'
            '87898034589777e77bfa610ed42e6663a6ba57bb91116d296f800199c1bb9183')

prepare() {
  bsdtar xvf "$pkgname-$pkgver-bitmaps.zip" -C "Bibata_Cursor-$pkgver"

  cd "Bibata_Cursor-$pkgver"
  rm -rf themes bin
}

build() {
  cd "Bibata_Cursor-$pkgver"

  _version="v$pkgver"

  _get_config_path() {
    local key="${1}"
    local cfg_path="configs"

    if [[ $key == *"Right"* ]]; then
      cfg_path="${cfg_path}/right"
    else
      cfg_path="${cfg_path}/normal"
    fi

    echo $cfg_path
  }

  _with_version() {
    local comment="${1}"
    echo "$comment ($_version)."
  }

  declare -A names
  names["Bibata-Modern-Amber"]=$(_with_version "Yellowish and rounded edge Bibata")
  names["Bibata-Modern-Amber-Right"]=$(_with_version "Yellowish and rounded edge right-hand Bibata")
  names["Bibata-Modern-Classic"]=$(_with_version "Black and rounded edge Bibata")
  names["Bibata-Modern-Classic-Right"]=$(_with_version "Black and rounded edge right-hand Bibata")
  names["Bibata-Modern-Ice"]=$(_with_version "White and rounded edge Bibata")
  names["Bibata-Modern-Ice-Right"]=$(_with_version "White and rounded edge right-hand Bibata")
  names["Bibata-Original-Amber"]=$(_with_version "Yellowish and sharp edge Bibata")
  names["Bibata-Original-Amber-Right"]=$(_with_version "Yellowish and sharp edge right-hand Bibata")
  names["Bibata-Original-Classic"]=$(_with_version "Black and sharp edge Bibata")
  names["Bibata-Original-Classic-Right"]=$(_with_version "Black and sharp edge right-hand Bibata")
  names["Bibata-Original-Ice"]=$(_with_version "White and sharp edge Bibata")
  names["Bibata-Original-Ice-Right"]=$(_with_version "White and sharp edge right-hand Bibata")

  for key in "${!names[@]}"; do
    comment="${names[$key]}"
    cfg_path=$(_get_config_path "$key")
    ctgen "$cfg_path/x.build.toml" -p x11 -d "bitmaps/$key" -n "$key" -c "$comment XCursors" &
    PID=$!
    wait $PID
  done
}

package() {
  cd "Bibata_Cursor-$pkgver"
  install -d "$pkgdir/usr/share/icons"
  cp -r themes/Bibata-* "$pkgdir/usr/share/icons/"
}
