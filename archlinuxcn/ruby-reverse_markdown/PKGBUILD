# Maintainer: mnussbaum <michaelnussbaum08@gmail.com>

_gemname=reverse_markdown
pkgname=ruby-reverse_markdown
pkgver=2.1.1
pkgrel=2
pkgdesc="Ruby gem to convert html into markdown"
arch=("any")
depends=(
  ruby
  ruby-nokogiri
  license-wtfpl
)
makedepends=(rubygems)
url="https://github.com/xijo/reverse_markdown"
noextract=($_gemname-$pkgver.gem)
license=("custom:WTFPL")
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
sha256sums=("b2206466b682ac1177b6b8ec321d00a84fca02d096c5d676a7a0cc5838dc0701")

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"

  gem install \
    --ignore-dependencies \
    --no-user-install \
    -i "$pkgdir/$_gemdir" \
    -n "$pkgdir/usr/bin" \
    $_gemname-$pkgver.gem

  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
}
