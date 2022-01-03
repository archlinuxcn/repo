# Maintainer: DDoSolitary <DDoSolitary@gmail.com>
# Contributor: Carsten Feuls <archlinux@carstenfeuls.de>

_gemname=travis
pkgname=ruby-$_gemname
pkgver=1.11.0
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
sha512sums=('b6db17b149a54f7ab3c5b79439b1385386bbfe0350816d303e7c74c0494be08451fdb14550cba7fb54df3a643a530f1434bb1ee0c3e28c492ac6e8f3baf3d558')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  find "$pkgdir" -name '*.gemspec' -type f -exec sed -i 's/\(launchy.*\), "< 2.5.0"/\1/' '{}' \;
  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
