# Maintainer: DDoSolitary <DDoSolitary@gmail.com>
# Contributor: Artem Vorotnikov <artem@vorotnikov.me>

_gemname=pusher-client
pkgname=ruby-$_gemname
pkgver=0.6.2
pkgrel=3
pkgdesc='Client for consuming WebSockets from http://pusher.com'
arch=(any)
url='http://github.com/pusher/pusher-ruby-client'
license=(MIT)
depends=(ruby ruby-websocket ruby-json)
makedepends=(ruby-rdoc)
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha512sums=('1d4a81027f08065c840c89098d562787c73c0f39fa986152bf22ee43fb222b8a26782fc4be3cf01acb9a62c5237cccb8515d2bfc6c4a4d9d1dc53b853599a30d')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE.txt"
}
