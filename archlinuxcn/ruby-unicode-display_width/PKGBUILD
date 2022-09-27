# Maintainer: mnussbaum <michaelnussbaum08@gmail.com>

_gemname=unicode-display_width
pkgname=ruby-${_gemname}
pkgver=2.3.0
pkgrel=1
pkgdesc="[Unicode 14.0.0] Determines the monospace display width of a string using EastAsianWidth.txt, Unicode general category, and other data"
arch=(any)
depends=(ruby)
url="https://rubygems.org/gems/unicode-display_width"
noextract=($_gemname-$pkgver.gem)
options=(!emptydirs)
license=(MIT)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
sha256sums=("4796ca01137fe8cf59cada263b74ebe6bb9583c555ec2239be4cb97c91064765")

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
