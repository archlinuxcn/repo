# Maintainer: DDoSolitary <DDoSolitary@gmail.com>
# Contributor: Carsten Feuls <archlinux@carstenfeuls.de>

_gemname=travis
pkgname=ruby-$_gemname
pkgver=1.10.0
pkgrel=1
pkgdesc='CLI and Ruby client library for Travis CI'
arch=(any)
url='https://github.com/travis-ci/travis.rb'
license=(MIT)
depends=(ruby ruby-backports ruby-faraday ruby-faraday-middleware ruby-gh ruby-highline ruby-json_pure ruby-launchy ruby-pusher-client ruby-pry)
makedepends=('ruby-rdoc')
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha512sums=('025e8cdf48100ff20d85925a6285993bda0d1651e145d554c2ec987c4557e2d3bc49da6529af4c577fcd9b88600549b3c12cff49b824d7fcb93a96a0c572603c')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  find "$pkgdir" -name '*.gemspec' -type f -exec sed -i 's/\(launchy.*\), "< 2.5.0"/\1/' '{}' \;
  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
