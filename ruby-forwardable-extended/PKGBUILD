# Maintainer: Carsten Feuls <archlinux@carstenfeuls.de>

_gemname=forwardable-extended
pkgname=ruby-$_gemname
pkgver=2.6.0
pkgrel=1
pkgdesc='Forwardable with hash, and instance variable extensions.'
arch=(any)
url='http://github.com/envygeeks/forwardable-extended'
license=(MIT)
depends=('ruby')
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha512sums=('e78eed0d6e06c0db4c692718425aa92bb0d87060fb3cc3207c24d9105437caa2d3c421867077567e87cd462e8d6c2f255b82e14e2249b224e5eca2c2240355b7')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
