# Maintainer: DDoSolitary <DDoSolitary@gmail.com>
# Contributor: Carsten Feuls <archlinux@carstenfeuls.de>

_gemname=websocket
pkgname=ruby-$_gemname
pkgver=1.2.8
pkgrel=2
pkgdesc='Universal Ruby library to handle WebSocket protocol'
arch=(any)
url='http://github.com/imanel/websocket-ruby'
license=(MIT)
depends=(ruby)
makedepends=(ruby-rdoc)
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha512sums=('42630e9d577a0fcbfa9f28ba487d12e4d96c59c615dddf91f810abc151a716aa9eaac3788999cb8eb2e729eff92fe8d262639b4b460029690994c710e78c138c')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
}
