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
pkgver=17.0.1
pkgrel=2
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
b2sums=('72c9417c37f4de670ba9f19327c3e87cdcc3f34110ef717edd941e1aa38684c02f6de4e69d399436c590dc76b86eae7db52e07251f4ff9a0df0a0c5cd976cd52'
        'b3280b0f5f1a0ed6528a5095cd172debbe13d3e4f2c407b87d51e3de1098cd2f5474eaedf8a2e3528c40a2f390ca37c7a3e3644bd6e0e7519d082e015b715b30'
        'fc76af253b91aa5d0a60c812c54aab9c91b04a7671e653b2ee8c80a116153e07d27a2dc10e257bd59434c384e68981dc151f2731dc48f96f20c104fd7ed8222f')

prepare() {
  cd "$pkgbase"
}

build() {
  cd "$pkgbase"
  cp ../twemoji.toml.tmpl .
  ../build.sh
  nanoemoji twemoji_*.toml
  cp build/Twemoji-CFF2-COLRv1.otf build/TwemojiALL.ttf
  maximum_color --bitmaps build/TwemojiALL.ttf
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
    "$pkgdir/usr/share/fonts/Twemoji.ttf"
  install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" \
    LICENSE-GRAPHICS
}
# vim: set ts=2 sw=2 et:
