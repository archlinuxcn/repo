# Maintainer: mnussbaum <michaelnussbaum08@gmail.com>

pkgname=ruby-rbs
_gemname=${pkgname#ruby-}
pkgver=3.1.0
pkgrel=1
pkgdesc="Describe the structure of Ruby programs"
arch=("any")
depends=(
  ruby
)
makedepends=(rubygems)
url="http://solargraph.org/"
noextract=($_gemname-$pkgver.gem)
license=("MIT")
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
sha256sums=('4ef8f22f3452aad28ca2ff61ede65a2a98b604e0365058293e749de91a74d07d')

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
