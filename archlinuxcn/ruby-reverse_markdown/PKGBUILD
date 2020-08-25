# Maintainer: mnussbaum <michaelnussbaum08@gmail.com>

_gemname=reverse_markdown
pkgname=ruby-reverse_markdown
pkgver=2.0.0
pkgrel=0
pkgdesc="Ruby gem to convert html into markdown"
arch=("any")
depends=(
  ruby
  ruby-nokogiri
)
makedepends=(rubygems)
url="https://github.com/xijo/reverse_markdown"
noextract=($_gemname-$pkgver.gem)
license=("WTFPL")
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
sha256sums=("8625d50ea04f09dfa49b74fd57d12f65cbeaa19bb14e81236d5b9092ced9ce70")

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
