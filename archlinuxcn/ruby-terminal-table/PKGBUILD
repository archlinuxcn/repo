# Maintainer: farawayer <farwayer@gmail.com>
# Co-Maintainer: Bert Peters <bert@bertptrs.nl>

_gemname=terminal-table
pkgname=ruby-$_gemname
pkgver=2.0.0
pkgrel=1
pkgdesc='Simple, feature rich ascii table generation library'
arch=(any)
url='https://github.com/tj/terminal-table'
license=(MIT)
depends=(
  ruby
  'ruby-unicode-display_width<2' 'ruby-unicode-display_width>=1.1.1'
)
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha1sums=('967467fe515e0221049431ef2929404bf9dc6be2')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
}
