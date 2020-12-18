# Maintainer: DDoSolitary <DDoSolitary@gmail.com>
# Contributor: Carsten Feuls <archlinux@carstenfeuls.de>

_gemname=websocket
pkgname=ruby-$_gemname
pkgver=1.2.9
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
sha512sums=('42044df313e1ca2525700decaac6f77b8bf9d4f1dd21723de408c636196e9f77c4b9d865abeb1de68575ad3b59ad48a9e7c30f0e16dbd15695958f8cf6ca3d57')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
}
