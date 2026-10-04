# Maintainer: Coelacanthus <uwu@coelacanthus.name>

pkgbase=twemoji-fonts
pkgname=(
  otf-twemoji-colrv0
  ttf-twemoji-colrv0
  otf-twemoji-colrv1
  ttf-twemoji-colrv1
  ttf-twemoji-cbdt
  otf-twemoji-all
)
pkgver=17.0.3
pkgrel=1
pkgdesc="Twemoji built with nanoemoji"
url="https://github.com/jdecked/twemoji"
arch=(any)
license=('CC-BY-4.0')
makedepends=(
  'awk'
  'git'
  'nanoemoji'
  'perl-rename'
  'pngquant'
  'resvg'
  'sed'
)
provides=('emoji-font')
source=(
  "$pkgbase::git+https://github.com/jdecked/twemoji.git#tag=v$pkgver"
  build.sh
  twemoji.toml.tmpl
)
b2sums=('5641c5166236035f2bc55cabec9640eea3f832a88586a072cb73c720ba880d1f0d8c6a0639526d4d774dbd4a9af971f96cc419e88be678c7a5369b720bb69f0c'
        '3a96dbeb6a809d6643b31b171d5c261f1880d00480dd5858d0a7685a2d1a39b94c88c7f8748b8acffac50b55e96dc41d03568be5956eddf02978cb24e570217e'
        'fc76af253b91aa5d0a60c812c54aab9c91b04a7671e653b2ee8c80a116153e07d27a2dc10e257bd59434c384e68981dc151f2731dc48f96f20c104fd7ed8222f')

prepare() {
  cd "$pkgbase"
}

build() {
  cd "$pkgbase"
  cp ../twemoji.toml.tmpl .
  ../build.sh
  nanoemoji twemoji_*.toml
  maximum_color --bitmaps --output_file $(realpath build/TwemojiALL.ttf) build/TwemojiCOLRv1.ttf
}

package_otf-twemoji-colrv0() {
  cd "$pkgbase"
  install -Dm644 "build/Twemoji-CFF-COLRv0.otf" \
    "$pkgdir/usr/share/fonts/Twemoji.otf"
  install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" \
    LICENSE-GRAPHICS
}
package_otf-twemoji-colrv1() {
  cd "$pkgbase"
  install -Dm644 "build/Twemoji-CFF2-COLRv1.otf" \
    "$pkgdir/usr/share/fonts/Twemoji.otf"
  install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" \
    LICENSE-GRAPHICS
}
package_ttf-twemoji-colrv0() {
  cd "$pkgbase"
  install -Dm644 "build/TwemojiCOLRv0.ttf" \
    "$pkgdir/usr/share/fonts/Twemoji.ttf"
  install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" \
    LICENSE-GRAPHICS
}
package_ttf-twemoji-colrv1() {
  cd "$pkgbase"
  install -Dm644 "build/TwemojiCOLRv1.ttf" \
    "$pkgdir/usr/share/fonts/Twemoji.ttf"
  install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" \
    LICENSE-GRAPHICS
}
package_ttf-twemoji-cbdt() {
  cd "$pkgbase"
  install -Dm644 "build/TwemojiCBDT.ttf" \
    "$pkgdir/usr/share/fonts/Twemoji.ttf"
  install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" \
    LICENSE-GRAPHICS
}
package_otf-twemoji-all() {
  cd "$pkgbase"
  install -Dm644 "build/TwemojiALL.ttf" \
    "$pkgdir/usr/share/fonts/Twemoji.otf"
  install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" \
    LICENSE-GRAPHICS
}
# vim: set ts=2 sw=2 et:
