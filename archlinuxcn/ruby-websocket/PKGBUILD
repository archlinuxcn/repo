# Maintainer: DDoSolitary <DDoSolitary@gmail.com>
# Contributor: Carsten Feuls <archlinux@carstenfeuls.de>

_gemname=websocket
pkgname=ruby-$_gemname
pkgver=1.2.11
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
sha512sums=('164e9707d7cb490502c82eb58ae5f2c70d16e04dbc5ce4467411d6ff76f2a2e158680ee013609289b48706baab8e1c72fb22dad6acd67fc09302e78832cb488c')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
}
