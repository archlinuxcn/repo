# Maintainer: farawayer <farwayer@gmail.com>
# Co-Maintainer: Bert Peters <bert@bertptrs.nl>

_gemname=terminal-table
pkgname=ruby-$_gemname
pkgver=3.0.0
pkgrel=2
pkgdesc='Simple, feature rich ascii table generation library'
arch=(any)
url='https://github.com/tj/terminal-table'
license=(MIT)
depends=(
  ruby
  'ruby-unicode-display_width>=1.1.1'
)
options=(!emptydirs)
source=($pkgname-$pkgver.tar.gz::https://github.com/tj/terminal-table/archive/v${pkgver}.tar.gz)
sha1sums=('71d5cb3645266244fe4a1daf0f0427d06907d8b7')

prepare() {
  cd ${_gemname}-${pkgver}
  sed -r 's|~>|>=|g' -i ${_gemname}.gemspec # don't give a fuck about rubys bla bla
  sed 's|git ls-files -z|find -type f -print0 \|sed "s,\\\\./,,g"|' -i ${_gemname}.gemspec
}

build() {
  cd ${_gemname}-${pkgver}
  gem build ${_gemname}.gemspec
}

package() {
  cd ${_gemname}-${pkgver}
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
}
