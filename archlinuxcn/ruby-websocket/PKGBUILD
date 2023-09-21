# Maintainer: DDoSolitary <DDoSolitary@gmail.com>
# Contributor: Carsten Feuls <archlinux@carstenfeuls.de>

_gemname=websocket
pkgname=ruby-$_gemname
pkgver=1.2.10
pkgrel=1
pkgdesc='Universal Ruby library to handle WebSocket protocol'
arch=(any)
url='http://github.com/imanel/websocket-ruby'
license=(MIT)
depends=(ruby)
makedepends=(ruby-rdoc)
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha512sums=('c06598a4988b1a4361ba55d807577c756d82295e5c5316fe9f0492a32776599b8ce878615c5c0d4ed2d70d37bfed5ec188398922dd140fd195b894262df63f57')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
}
