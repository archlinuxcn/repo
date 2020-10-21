# Maintainer: DDoSolitary <DDoSolitary@gmail.com>
# Contributor: Rhys Davies <rhys@johnguant.com>

_gemname=gh
pkgname=ruby-$_gemname
pkgver=0.18.0
pkgrel=1
pkgdesc='layered github client'
arch=(any)
url='https://github.com/travis-ci/gh'
license=(MIT)
depends=(ruby ruby-activesupport-5 ruby-addressable ruby-faraday ruby-faraday-middleware ruby-multi_json ruby-net-http-persistent ruby-net-http-pipeline)
makedepends=(ruby-rdoc)
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha512sums=('f0b04bf32db52ebb1b27714dacb00e07c78115fbe60681df06f3f503d41c62c683245cee6653480dcb865f0292f2fa85c4b62c0a85e230953606af517b76b045')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  sed -i 's/~>/>=/g' "$pkgdir/$_gemdir/specifications/$_gemname-$pkgver.gemspec"
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
