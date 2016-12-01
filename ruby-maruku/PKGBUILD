# Maintainer: Mario Finelli <mario dot finelli at yahoo dot com>
# Contributor: Anatol Pomozov <anatol.pomozov at gmail dot com>
# Contributor: oliparcol <oliparcol at gmail dot com>

_gemname=maruku
pkgname=ruby-$_gemname
pkgver=0.7.2
pkgrel=3
pkgdesc='Maruku is a Markdown-superset interpreter written in Ruby.'
arch=(any)
url='http://github.com/bhollis/maruku'
license=(MIT)
depends=(ruby)
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha256sums=('e8a755d8e9c24f1601157c8b376f0378f88d487fa777aa655f332504557a0798')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/MIT-LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/MIT-LICENSE.txt"
}
