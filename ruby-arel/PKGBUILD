# Maintainer: Carsten Feuls <archlinux@carstenfeuls.de>

_gemname=arel
pkgname=ruby-$_gemname
pkgver=9.0.0
pkgrel=1
pkgdesc='Arel Really Exasperates Logicians  Arel is a SQL AST manager for Ruby'
arch=(any)
url='https://github.com/rails/arel'
license=(MIT)
depends=(ruby)
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha512sums=('f722f4b0aa9a83698f4f7d4791c5c298d2893274eab9ad74f6b1ec903d884220157d00d6f205968805ad30d99e466758c315ecd115a81df6fdecb44f1ca9e32b')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/MIT-LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/MIT-LICENSE.txt"
}
