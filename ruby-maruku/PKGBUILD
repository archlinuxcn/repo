# Maintainer: Mario Finelli <mario dot finelli at yahoo dot com>
# Contributor: Anatol Pomozov <anatol.pomozov at gmail dot com>
# Contributor: oliparcol <oliparcol at gmail dot com>

_gemname=maruku
pkgname=ruby-$_gemname
pkgver=0.7.3
pkgrel=1
pkgdesc='Maruku is a Markdown-superset interpreter written in Ruby.'
arch=(any)
url='http://github.com/bhollis/maruku'
license=(MIT)
depends=(ruby)
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha256sums=('dd14156f57b5433993710adca63b766d18b36f6e35cb25c21b178a6edfedebe4')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/MIT-LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/MIT-LICENSE.txt"
}
