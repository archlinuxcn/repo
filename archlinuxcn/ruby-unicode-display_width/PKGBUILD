# Maintainer: mnussbaum <michaelnussbaum08@gmail.com>

_gemname=unicode-display_width
pkgname=ruby-${_gemname}
pkgver=2.0.0
pkgrel=1
pkgdesc="[Unicode 13.0.0] Determines the monospace display width of a string using EastAsianWidth.txt, Unicode general category, and other data"
arch=(any)
depends=(ruby)
url="https://rubygems.org/gems/unicode-display_width"
noextract=($_gemname-$pkgver.gem)
options=(!emptydirs)
license=(MIT)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
sha256sums=("55ec39f2a0bb8c8c3f0480200b28edbedd70473c27b84c5359531a89985d34ae")

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install \
    --ignore-dependencies \
    --no-user-install \
    -i "$pkgdir/$_gemdir" \
    -n "$pkgdir/usr/bin" \
    $_gemname-$pkgver.gem

  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"

  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/MIT-LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
