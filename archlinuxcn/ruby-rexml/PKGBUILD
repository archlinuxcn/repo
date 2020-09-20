# Maintainer: Mario Finelli <mario at finel dot li>

_gemname=rexml
pkgname=ruby-${_gemname}
pkgver=3.2.4
pkgrel=1
pkgdesc="An XML toolkit for Ruby"
arch=('any')
depends=(ruby)
makedepends=(rubygems ruby-rdoc)
url="https://github.com/ruby/rexml"
noextract=($_gemname-$pkgver.gem)
license=(BSD)
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
sha256sums=('036b31f3c052be42b7a2e6914f3322daaecce46b172806f38fea4297389b7bd6')

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
