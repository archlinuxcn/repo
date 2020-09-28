# Maintainer: Mario Finelli <mario at finel dot li>

_gemname=rubocop-ast
pkgname=ruby-${_gemname}
pkgver=0.7.1
pkgrel=1
pkgdesc="RuboCop's Node and NodePattern classes."
arch=('any')
depends=(
  ruby
  ruby-parser
)
makedepends=(rubygems ruby-rdoc)
url="https://rubocop.readthedocs.io"
noextract=($_gemname-$pkgver.gem)
license=('MIT')
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
sha256sums=('e4d04cca95f5e023fec1c3c03e3fad048209803fbb8413c0031631aec97f3089')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"

  gem install \
    --ignore-dependencies \
    --no-user-install \
    -i "$pkgdir/$_gemdir" \
    -n "$pkgdir/usr/bin" \
    $_gemname-$pkgver.gem

  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"

  install -Dm0644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/LICENSE.txt" \
    "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
