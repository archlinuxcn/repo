# Maintainer: farwayer <farwayer@gmail.com>

_gemname=unicode-display_width
pkgname=ruby-${_gemname}
pkgver=1.7.0
pkgrel=1
pkgdesc='[Unicode 13.0.0] Determines the monospace display width of a string using EastAsianWidth.txt, Unicode general category, and other data.'
arch=(any)
depends=(ruby)
url='https://rubygems.org/gems/${_gemname}'
noextract=($_gemname-$pkgver.gem)
options=(!emptydirs)
license=(MIT)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
sha1sums=('6d743a99b24181c979b99f09df161fb2a2d983bf')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/MIT-LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
