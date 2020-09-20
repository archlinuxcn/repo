# Maintainer: Mario Finelli <mario at finel dot li>
# Contributor: Andy Weidenbaum <archbaum at gmail dot com>

_gemname=ruby-progressbar
pkgname=ruby-$_gemname
pkgver=1.10.1
pkgrel=1
pkgdesc="Flexible text progress bar library for Ruby."
arch=('any')
url="https://github.com/jfelchner/ruby-progressbar"
license=('MIT')
depends=('ruby')
makedepends=('ruby-rdoc')
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
sha256sums=('ee23400615f91c2ce6bc1e3bfa98392302ef38cbba8ad6de1bc26a4e1a88e7cc')
noextract=($_gemname-$pkgver.gem)
options=(!emptydirs)

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
